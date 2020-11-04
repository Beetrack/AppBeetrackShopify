from flask import Flask, request, redirect, render_template, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configurations import Configurations as cfg
import mysql.connector
import os
import ipdb
import json
import requests

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

@app.route('/install', methods= ['GET'])
def install():

    if request.args.get('shop'):
        shop = request.args.get('shop')

    else: 
        return Response(response="Error: Parameter shop Not Found", status= 500)

    auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
        shop, cfg.SHOPIFY_CFG['API_KEY'], cfg.SHOPIFY_CFG['SCOPE'], cfg.SHOPIFY_CFG['REDIRECT_URI'])
     
    return redirect(auth_url)

@app.route('/connect', methods= ['GET', 'POST'])  
def connect():

    if request.args.get('shop'):

        params = {
            "client_id" : cfg.SHOPIFY_CFG['API_KEY'],
            "client_secret" : cfg.SHOPIFY_CFG['API_SECRET'],
            "code" : request.args.get("code")
        }

        resp = requests.post("https://{0}/admin/oauth/access_token".format(request.args.get('shop')), data=params)
        resp_dict = json.loads(resp.text)

        access_token = resp_dict.get("access_token")
        shop = request.args.get('shop')

        session['access_token'] = access_token
        session['shop'] = shop

        return render_template('configuration.html')

    else:
        print("Failed to get access token: ", resp.status.code, resp.text)
        return render_template('error.html')

@app.route('/configuration', methods= ['GET', 'POST'])
def add_api_key():
    if request.method == 'POST':
        post_api_key = request.form['api_key']

        shop = session['shop']
        new_shop = Shops(name=shop)
        db.session.add(new_shop)
        db.session.commit()

        access_token = session['access_token']
        shop_id = new_shop.id
        user_name = new_shop.name
        shop_obj = Shops.query.get(shop_id)
        new_shopify_credential = Shopify_credentials(user_name=user_name, token=access_token, 
        shop_id_shopify=shop_obj)
        db.session.add(new_shopify_credential)
        db.session.commit()

        new_beetrack_credential = Beetrack_credentials(api_key=post_api_key, account_uuid='XXXX',
        shop_id_beetrack=shop_obj)
        db.session.add(new_beetrack_credential)
        db.session.commit()

        return render_template('connected.html')









if __name__ == "__main__":
    app.run(debug= True, port= 5000)   
