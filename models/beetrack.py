from db import db
import requests
from models.properties import Properties
from sqlalchemy import event

class BeetrackCredentialsModel(db.Model, Properties):

    __tablename__ = "beetrack_credentials"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_key = db.Column(db.String(255))
    account_uuid = db.Column(db.String(255))
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    shop = db.relationship("ShopsModel", back_populates = "beetrack_credentials")

    def __repr__(self):
        return 'Beetrack_credential ' + str(self.id)

    def __init__(self, api_key, account_uuid, shop_id_beetrack):
        self.api_key = api_key
        self.account_uuid = account_uuid
        self.shop_id_beetrack = shop_id_beetrack
        Properties.__init__(self)
    
    def serialize(self):
        return {
            "api_key": self.api_key,
            "account_uuid": self.account_uuid,
            "shop_id_beetrack": self.shop_id
            }

    @classmethod
    def find_by_uuid(cls, account_uuid):
        return cls.query.filter_by(account_uuid = account_uuid).first()
