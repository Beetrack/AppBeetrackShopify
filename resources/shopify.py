from flask_restful import Resource
from models.shopify import ShopifyCredentialsModel
from models.beetrack import BeetrackCredentialsModel

class Shopify(Resource):

    def get(self, user_name):
        shopify_credentials = ShopifyCredentialsModel.find_by_user_name(user_name)
        shop_id = shopify_credentials.shop_id
        beetrack_credentials = BeetrackCredentialsModel.find_by_shop_id(shop_id)
        if beetrack_credentials:
            return beetrack_credentials.json()
        return {'message': 'Shopify credentials not found'}, 404

    