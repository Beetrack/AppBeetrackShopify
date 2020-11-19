from db import db
from sqlalchemy import event, exists
from signals.beetrack import before_commit
from models.properties import Properties


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
