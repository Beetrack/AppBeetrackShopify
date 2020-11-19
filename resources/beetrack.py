from flask_restful import Resource
from models.beetrack import BeetrackCredentialsModel
from models.shopify import ShopifyCredentialsModel
import ipdb

class Beetrack(Resource):

    def get(self, account_uuid):

        beetrack_credential_obj = BeetrackCredentialsModel.find_by_uuid(account_uuid)
        shop_id = beetrack_credential_obj.shop_id
        shopify_credential_obj = ShopifyCredentialsModel.find_by_shop_id(shop_id)

        if shopify_credential_obj:
            ipdb.set_trace()
            return shopify_credential_obj.serialize
            
        return {'message': 'Shopify credentials were not found for these Beetrack uuid account'}, 404
