from flask_restful import Resource
from models.shopify import ShopifyCredentialsModel

class Shopify(Resource):

    def get(self, user_name):
        shopify_credentials_obj = ShopifyCredentialsModel.find_by_user_name(user_name)
        try:
            beetrack_credentials_obj = shopify_credentials_obj.shop.beetrack_credentials.pop()
            if shopify_credentials_obj or beetrack_credentials_obj:
                return beetrack_credentials_obj.serialize()
        except:
            return {'Message': 'Beetrack Credentials were not found for Shopify Username'}, 404
