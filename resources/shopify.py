from flask_restful import Resource
from models.shopify import ShopifyCredentialsModel
from models.beetrack import BeetrackCredentialsModel

class Shopify(Resource):

    def get(self, user_name):
        shopify_credentials_obj = ShopifyCredentialsModel.find_by_user_name(user_name)
        beetrack_credentials_obj = shopify_credentials_obj.shop.beetrack_credentials.pop()
        if shopify_credentials_obj or beetrack_credentials_obj:
            return beetrack_credentials_obj.beetrack_obj_jsonify()
        return {'message': 'Beetrack credentials were not found for these Shopify username'}, 404
