import uuid
from db import db
from flask import Blueprint, request, session, render_template, redirect
from api.shopify import ShopifyApiHandler
from models.shops import ShopsModel
from models.shopify import ShopifyCredentialsModel
from models.beetrack import BeetrackCredentialsModel

connection = Blueprint('connection', __name__)

@connection.route('/connect', methods= ['GET', 'POST'])
def connect():
    if "shop" in session:
        if not 'access_token' in session:
            try:
                code = request.args.get("code")
                shop = session["shop"]
                new_shop = ShopsModel(name=shop)
                new_shop.save_to_db()
                get_shopify_token = ShopifyApiHandler(shop).get_access_token(code)
                session['shopify_token'] = get_shopify_token
                new_shopify_credential = ShopifyCredentialsModel(user_name=shop, token=get_shopify_token, shop_id_shopify=new_shop)
                new_shopify_credential.save_to_db()
                beetrack_api_key = session["beetrack_api_key"]
                account_uuid = str(uuid.uuid4())
                session['account_uuid'] = account_uuid
                new_beetrack_credential = BeetrackCredentialsModel(api_key=beetrack_api_key, account_uuid=account_uuid, shop_id_beetrack=new_shop)
                new_beetrack_credential.save_to_db()
                return redirect('/webhooks')
            except:
                return render_template('information.html')
        else: 
            return render_template('configuration.html')
    else:
        print("Failed to get access token: ")
        return render_template('error.html')
