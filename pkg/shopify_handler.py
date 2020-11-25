import requests, json
from pkg.services.lastmile_api import LastMileApi
from flask_sqlalchemy import SQLAlchemy
from models.shopify import ShopifyCredentialsModel
import ipdb

def create_shopify_dispatch(shop_user_name, shopify_costumer_info, shopify_items):
    lastmile_api = LastMileApi()
    #shopify_credentials_obj = ShopifyCredentialsModel.find_by_user_name(shop_user_name)
    #beetrack_credentials_obj = shopify_credentials_obj.shop.beetrack_credentials.pop()
    #beetrack_credentials = beetrack_credentials_obj.serialize()
    beetrack_credentials = requests.get("http://localhost:5000/shopify_credentials/" + str(shop_user_name)).json()
    beetrack_api_key = beetrack_credentials["api_key"]
    new_dispatch = {
            "identifier": shopify_costumer_info[0],
            "contact_name": shopify_costumer_info[1],
            "contact_address": shopify_costumer_info[2],
            "contact_phone": shopify_costumer_info[3],
            "contact_email": shopify_costumer_info[4],
            "items": shopify_items,
            "tags": [
                {"name" :"id_order_shopify",
                "value": shopify_costumer_info[5]}, 
                {"name": "id_fulfilled",
                "value": shopify_costumer_info[6]}
                ]
            }
    print(new_dispatch)
    create = lastmile_api.create_dispatch(beetrack_api_key, new_dispatch)

    return create