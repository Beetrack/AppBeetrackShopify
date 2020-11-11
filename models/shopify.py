from db import db

class ShopifyCredentialsModel(db.Model):
    __tablename__ = "shopify_credentials"
    id = db.Column(db.Integer, primary_key = True , autoincrement = True)
    user_name = db.Column(db.String(255))
    token = db.Column(db.String(255))
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))

    def __repr__(self):
        return 'Shopify_credential ' + str(self.id)

    def __init__(self, user_name, token, shop_id_shopify):
        self.user_name = user_name
        self.token = token
        self.shop_id_shopify = shop_id_shopify

    def json(self):
        return {'token': self.token}

    @classmethod
    def find_by_user_name(cls, user_name):
        return cls.query.filter_by(user_name= user_name).first()

    @classmethod
    def find_by_shop_id(cls, shop_id):
        return cls.query.filter_by(shop_id= shop_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
