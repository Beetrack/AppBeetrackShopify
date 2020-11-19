from db import db
from flask import redirect
from sqlalchemy import event
from models.properties import Properties
import ipdb


class ShopsModel(db.Model, Properties):

    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable= False, unique= True)

    shopify_credentials = db.relationship('ShopifyCredentialsModel', backref = 'shop_id_shopify', lazy = 'select')
    beetrack_credentials = db.relationship('BeetrackCredentialsModel', backref = 'shop_id_beetrack', lazy = 'select')

    def __repr__(self):
        return 'Shop ' + str(self.id)

    def __init__(self, name):
        self.name = name
        Properties.__init__(self)
        #event.listen(session, 'before_commit', before_commit)

@event.listens_for(ShopsModel, 'before_insert')
def verify_shop(mapper, connection, target):
    shop = target.name
    verify_shop_name = ShopsModel.query.filter_by(name = shop).first()
    if verify_shop_name == None:
        return True
    else:
        raise Exception('Invalid Shop Name')