from flask_restful import Resource
from models.beetrack import BeetrackCredentialsModel

class Beetrack(Resource):

    def get(self, account_uuid):
        beetrack_credential_obj = BeetrackCredentialsModel.find_by_uuid(account_uuid)
        try:
            shopify_credential_obj = beetrack_credential_obj.shop.shopify_credentials.pop()
            if beetrack_credential_obj or shopify_credential_obj:
                return shopify_credential_obj.serialize()
        except:
            return {'Message': 'Shopify Credentials were not found for Beetrack UUID Account'}, 404
