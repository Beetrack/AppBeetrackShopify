from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from config import Config as cfg
import requests
import json

app = Flask(__name__, template_folder = "templates")
app.debug = True
app.secret_key  = cfg.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///merchants.db'
db = SQLAlchemy(app)

class Tienda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shops = db.Column(db.String(200), unique = True, nullable=False)
    access_token = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return "Shops " + str(self.id)

@app.route('/install', methods=['GET'])
def install ():
    """
    Connect a shopify store
    """
    if request.args.get('shop'):
        shop = request.args.get('shop')
    else:
        return Response(response='Error: parameter shop not found', status=500)

    auth_url = 'https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}'.format(
        shop, cfg.SHOPIFY_CONFIG['API_KEY'], cfg.SHOPIFY_CONFIG['SCOPE'], cfg.SHOPIFY_CONFIG['REDIRECT_URI']
    )
    print('Debug - auth URL: ', auth_url)
    return redirect(auth_url)

@app.route('/connect', methods=['GET'])
def connect():
    shop = request.args.get('shop')
    print(shop)
    if request.args.get('shop'):
        params = {
            'client_id': cfg.SHOPIFY_CONFIG['API_KEY'],
            'client_secret': cfg.SHOPIFY_CONFIG['API_SECRET'],
            'code': request.args.get('code')
        }
        resp = requests.post('https://{0}/admin/oauth/access_token'.format(request.args.get('shop')), data=params)
        resp_dict = json.loads(resp.text)
        acces_token = resp_dict.get("access_token")
        print(resp_dict, acces_token)

        if 200 == resp.status_code:
            shop_name = shop
            api_token = acces_token
            new_shop = Tienda(shops=shop_name, access_token=api_token)
            db.session.add(new_shop)
            db.session.commit()
            resp_json = json.loads(resp.text)
            return render_template('welcome.html')

        else:
            print('Failed to get access token: ', resp.status_code, resp.text)
            return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)