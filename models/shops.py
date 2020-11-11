from db import db

# Shops table
class ShopsModel(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable= False, unique= True)

    shopify_credentials = db.relationship('ShopifyCredentialsModel', backref = 'shop_id_shopify', lazy = 'select')
    beetrack_credentials = db.relationship('BeetrackCredentialsModel', backref = 'shop_id_beetrack', lazy = 'select')

    def __repr__(self):
        return 'Shop ' + str(self.id)

    def __init__(self, name):
        self.name = name 

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()