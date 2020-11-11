from flask_restful import Resource
from models.beetrack import BeetrackCredentialsModel

class Beetrack(Resource):

    def get(self, account_uuid):
        beetrack_credential = BeetrackCredentialsModel.find_by_uuid(account_uuid)
        if beetrack_credential:
            return beetrack_credential.json()
        return {'message': 'Beetrack credentials not found'}, 404

    