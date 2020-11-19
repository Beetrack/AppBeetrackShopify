from db import db
from models.shops import ShopsModel
from models.properties import Properties

class ShopifyCredentialsModel(db.Model, Properties):

    __tablename__ = "shopify_credentials"
    
    id = db.Column(db.Integer, primary_key = True , autoincrement = True)
    user_name = db.Column(db.String(255))
    token = db.Column(db.String(255))
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    shop = db.relationship("ShopsModel", back_populates = "shopify_credentials")

    def __repr__(self):
        return 'Shopify_credential ' + str(self.id)

    def __init__(self, user_name, token, shop_id_shopify):
        self.user_name = user_name
        self.token = token
        self.shop_id_shopify = shop_id_shopify
        Properties.__init__(self)

    def serialize(self):
        return {
            "user_name": self.user_name,
            "token": self.token,
            "shop_id_shopify": self.shop_id
            }

    @classmethod
    def find_by_user_name(cls, user_name):
        return cls.query.filter_by(user_name= user_name).first()
