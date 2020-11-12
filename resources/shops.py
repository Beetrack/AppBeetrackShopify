from flask_restful import Resource
from models.shops import ShopsModel

class Shops(Resource):

    def get(self, name):

        shop = ShopsModel.find_by_name(name)

        if shop:
            return shop.json()
            
        return {'message': 'Shop not found'}, 404
