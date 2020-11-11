from flask_restful import Resource
from models.shopify import ShopifyCredentialsModel

class Shopify(Resource):

    def get(self, user_name):
        shopify_credatials = ShopifyCredentialsModel.find_by_user_name(user_name)
        if shopify_credatials:
            return shopify_credatials.json()
        return {'message': 'Shopify credentials not found'}, 404

    