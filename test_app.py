from flask import Flask, render_template, request, redirect, Response, session
from configuration import Configuration as cfg
from flask_sqlalchemy import SQLAlchemy 
import requests
import json


app = Flask(__name__, template_folder="templates")
app.debug = True
app.secret_key = cfg.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shops.db'
db = SQLAlchemy(app)

class Shops(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    shop = db.Column(db.String(200), unique = True, nullable=False)
    access_token = db.Column(db.String(200), unique=True, nullable=False)
    
    def __repr__(self):
        return "Shop " + str(self.id)

"""class API_Key(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    api_key = db.Column(db.String(300), unique = True, nullable=False)

    def __repr__(self):
        return "Shop " + str(self.id)"""

@app.route('/install')
def install():
    if request.args.get('shop'):
        shop = request.args.get('shop')
    else:
        return Response(response="Error: Parameter shop Not Found", status= 500)

    auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
        shop, cfg.SHOPIFY_CONFIGURATION['API_KEY'], cfg.SHOPIFY_CONFIGURATION['SCOPE'], cfg.SHOPIFY_CONFIGURATION['REDIRECT_URI'])

    print("Debug - auth URL: ", auth_url)
    
    return  redirect(auth_url)

@app.route('/connect', methods= ['POST','GET'])
def connect():
    shop = request.args.get('shop')
    session['shop'] = shop
    if request.args.get('shop'):
        params = {
            "client_id" : cfg.SHOPIFY_CONFIGURATION['API_KEY'],
            "client_secret" : cfg.SHOPIFY_CONFIGURATION['API_SECRET'],
            "code" : request.args.get("code")
        }
        resp = requests.post("https://{0}/admin/oauth/access_token".format(request.args.get('shop')), data=params)
        resp_dict = json.loads(resp.text)
        access_token = resp_dict.get("access_token")
        print(resp_dict, access_token)

        if 200 == resp.status_code:
            shop_name = shop
            api_token = access_token
            new_shop = Shops(shop= shop_name, access_token= api_token)
            db.session.add(new_shop)
            db.session.commit()
            return render_template('home.html')
        else:
            print("Failed to get access token: ", resp.status.code, resp.text)
            return render_template('error.html')

@app.route('/connected')
def connected():
    print('Shop ', session['shop'])
    return render_template('connected.html')

@app.route('/connect/api_key', methods= ['POST','GET'])
def save_api_key():
    if request.method == 'POST':
        post.api_key = request.form['api_key']
        new_api_key = API_Key(api_key= post_api_key)
        db.session.add(new_api_key)
        db.session.commit()
        return redirect('/home')
    else:
        return render_template('connect.html')


if __name__ == "__main__":
    app.run(debug= True, port= 5000)
