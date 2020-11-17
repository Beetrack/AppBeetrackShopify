from db import db
from sqlalchemy import event
from signals.beetrack import before_commit

class ShopsModel(db.Model):

    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable= False, unique= True)

    shopify_credentials = db.relationship('ShopifyCredentialsModel', backref = 'shop_id_shopify', lazy = 'select')
    beetrack_credentials = db.relationship('BeetrackCredentialsModel', backref = 'shop_id_beetrack', lazy = 'select')

    def __repr__(self):
        return 'Shop ' + str(self.id)

    def __init__(self, session, name):
        self.name = name
        event.listen(session, 'before_commit', before_commit) 

    #Dejar en una clase intermedia
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
