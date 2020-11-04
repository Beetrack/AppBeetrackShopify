from flask import Flask, request, redirect, render_template, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configurations import Configurations as cfg
from api.shopify import ShopifyApiHandler
from api.beetrack import BeetrackApiHandler
import mysql.connector, os, ipdb, json, requests, uuid


app = Flask(__name__)
app.debug = True
app.secret_key = '12334abcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
    cfg.DB_CFG['DB_USER_NAME'], cfg.DB_CFG['DB_PASS'], cfg.DB_CFG['DB_HOST'], cfg.DB_CFG['DB_NAME'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Shops(db.Model):

    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable= False, unique= True)
    shopify_credentials = db.relationship('Shopify_credentials', backref='shop_id_shopify', lazy='select')
    beetrack_credentials = db.relationship('Beetrack_credentials', backref='shop_id_beetrack', lazy='select')
    homologation_configurations = db.relationship('Homologation_configurations', backref='shop_id_homo', lazy='select')


    def __repr__(self):
        return 'Shop ' + str(self.id)

class Shopify_credentials(db.Model):

    __tablename__ = "shopify_credentials"

    id = db.Column(db.Integer,primary_key=True ,autoincrement=True)
    user_name = db.Column(db.String(255))
    token = db.Column(db.String(255))

    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))

    def __repr__(self):
        return 'Shopify_credential ' + str(self.id)

class Beetrack_credentials(db.Model):

    __tablename__ = "beetrack_credentials"

    id = db.Column(db.Integer,primary_key=True ,autoincrement=True)
    api_key = db.Column(db.String(255))
    account_uuid = db.Column(db.String(255))

    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))

    def __repr__(self):
        return 'Beetrack_credential ' + str(self.id)

class Homologation_configurations(db.Model):

    __tablename__ = "omologation_configurations"

    id = db.Column(db.Integer,primary_key=True ,autoincrement=True)
    account_configuration = db.Column(db.Text())

    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))

    def __repr__(self):
        return 'Homologation_configuration ' + str(self.id)

@app.route('/configuration', methods= ['GET', 'POST'])
def add_api_key():
    shop = request.args.get('shop')
    session['shop'] = shop

    if request.method == 'POST':
        beetrack_api_key = request.form['api_key']
        verify = BeetrackApiHandler(beetrack_api_key).verify_apikey()
        if verify == True:
            session["beetrack_api_key"] = beetrack_api_key
            return redirect('/install')
        else:
            #Crear un template para manejar el error de llave API
            return render_template('error.html')

@app.route('/install', methods= ['GET'])
def install():
    if "shop" in session:
        shop = session["shop"]
    else: 
        return Response(response="Error: Parameter shop Not Found", status= 500)

    auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
        shop, cfg.SHOPIFY_CFG['API_KEY'], cfg.SHOPIFY_CFG['SCOPE'], cfg.SHOPIFY_CFG['REDIRECT_URI'])
    return redirect(auth_url)

@app.route('/connect', methods= ['GET', 'POST'])  
def connect():
    if "shop" in session:
        if not 'access_token' in session:
            shop = session["shop"]
            code = request.args.get("code")
            get_shopify_token = ShopifyApiHandler().get_access_token(shop, code)
            new_shop = Shops(name=shop)
            db.session.add(new_shop)
            db.session.commit()

            shop_id = new_shop.id
            user_name = new_shop.name
            shop_obj = Shops.query.get(shop_id)
            new_shopify_credential = Shopify_credentials(user_name=user_name, token=get_shopify_token, shop_id_shopify=shop_obj)
            db.session.add(new_shopify_credential)
            db.session.commit()

            account_uuid = str(uuid.uuid4())
            beetrack_api_key = session["beetrack_api_key"]
            new_beetrack_credential = Beetrack_credentials(api_key=beetrack_api_key, account_uuid=account_uuid, shop_id_beetrack=shop_obj)
            db.session.add(new_beetrack_credential)
            db.session.commit()
            return render_template('connected.html')
        else: 
            return render_template('configuration.html')

    else:
        print("Failed to get access token: ")
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug= True, port= 5000)   
