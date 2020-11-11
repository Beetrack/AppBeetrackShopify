from flask_restful import Resource
from models.beetrack import BeetrackCredentialsModel
from models.shopify import ShopifyCredentialsModel

class Beetrack(Resource):

    def get(self, account_uuid):
        beetrack_credential = BeetrackCredentialsModel.find_by_uuid(account_uuid)
        shop_id = beetrack_credential.shop_id
        shopify_credential = ShopifyCredentialsModel.find_by_shop_id(shop_id)
        if shopify_credential:
            return shopify_credential.json()
        return {'message': 'Beetrack credentials not found'}, 404

    