from flask import Flask, request, redirect, render_template, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configurations import Configurations as cfg
from api.shopify import ShopifyApiHandler
from api.beetrack import BeetrackApiHandler
import mysql.connector, os, ipdb, json, requests, uuid
from db import db
from models.shops import ShopsModel
from models.shopify import ShopifyCredentialsModel
from models.beetrack import BeetrackCredentialsModel

app = Flask(__name__)
app.secret_key = '12334abcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
    cfg.DB_CFG['DB_USER_NAME'], cfg.DB_CFG['DB_PASS'], cfg.DB_CFG['DB_HOST'], cfg.DB_CFG['DB_NAME'])
# Migration
#migrate = Migrate(app, db)

@app.route('/configuration', methods= ['GET', 'POST'])
def add_api_key():
    if request.method == "GET":
        shop = request.args.get('shop')
        session['shop'] = shop
        return render_template("configuration.html")

    elif request.method == 'POST':
        beetrack_api_key = request.form['api_key']
        verify = BeetrackApiHandler(beetrack_api_key).verify_apikey()
        if verify == True:
            session["beetrack_api_key"] = beetrack_api_key
            return redirect('/install')
        else:
            #Crear un template para manejar el error de llave API
            return render_template('error.html')
    else:
         return render_template('error.html')

@app.route('/install', methods= ['GET'])
def install():
    if "shop" in session:
        shop = session["shop"]
        auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
            shop,
            cfg.SHOPIFY_CFG['API_KEY'],
            cfg.SHOPIFY_CFG['SCOPE'],
            cfg.SHOPIFY_CFG['REDIRECT_URI']
            )
        return redirect(auth_url)
    else: 
        return Response(response="Error: Parameter shop Not Found", status= 500)

@app.route('/connect', methods= ['GET', 'POST'])  
def connect():
    if "shop" in session:
        if not 'access_token' in session:
            shop = session["shop"]
            code = request.args.get("code")
            get_shopify_token = ShopifyApiHandler(shop).get_access_token(code)
            session['shopify_token'] = get_shopify_token
            new_shop = ShopsModel(name=shop)
            new_shop.save_to_db()

            shop_id = new_shop.id
            print(shop_id)
            user_name = new_shop.name
            shop_obj = ShopsModel.query.get(shop_id)
            new_shopify_credential = ShopifyCredentialsModel(user_name=user_name, token=get_shopify_token, shop=shop_obj)
            new_shopify_credential.save_to_db()

            account_uuid = str(uuid.uuid4())
            beetrack_api_key = session["beetrack_api_key"]
            new_beetrack_credential = BeetrackCredentialsModel(api_key=beetrack_api_key, account_uuid=account_uuid, shop=shop_obj)
            new_beetrack_credential.save_to_db()

            return redirect('/webhooks')
        else: 
            return render_template('configuration.html')

    else:
        print("Failed to get access token: ")
        return render_template('error.html')

@app.route('/webhooks')
def webhooks_shopify():
    if 'shop' and 'shopify_token' in session:
        shop = session["shop"]
        shopify_token = session['shopify_token']
        create_shopify_webhook = ShopifyApiHandler(shop).create_webhook(shopify_token,)
        if create_shopify_webhook == True:
            return render_template('connected.html')
        else:
            return render_template('error.html')
    else:
        return redirect('/connect')

# Run Server
if __name__ == "__main__":
    db.init_app(app)
    app.run(debug= True, port= 5000)

