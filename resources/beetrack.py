from flask_restful import Resource
from models.beetrack import BeetrackCredentialsModel
from models.shopify import ShopifyCredentialsModel

class Beetrack(Resource):

    def get(self, account_uuid):
        beetrack_credential_obj = BeetrackCredentialsModel.find_by_uuid(account_uuid)
        if beetrack_credential_obj:
            shop_id = beetrack_credential_obj.shop_id
            shopify_credential_obj = ShopifyCredentialsModel.find_by_shop_id(shop_id)
            if shopify_credential_obj:
                return shopify_credential_obj.shopify_obj_jsonify()
        return {'message': 'Shopify credentials were not found for these Beetrack uuid account'}, 404
