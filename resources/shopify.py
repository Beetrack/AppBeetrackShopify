from flask_restful import Resource
from models.shopify import ShopifyCredentialsModel
from models.beetrack import BeetrackCredentialsModel
from flask import jsonify
import ipdb
import json

class Shopify(Resource):

    def get(self, user_name):
        shopify_credentials_obj = ShopifyCredentialsModel.find_by_user_name(user_name)
        shop_id = shopify_credentials_obj.shop_id
        beetrack_credentials_obj = BeetrackCredentialsModel.find_by_shop_id(shop_id)
        
        if beetrack_credentials_obj:
            return beetrack_credentials_obj.serialize
            
        return {'message': 'Beetrack credentials were not found for these Shopify username'}, 404
