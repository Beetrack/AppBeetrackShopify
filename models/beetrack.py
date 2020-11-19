from db import db

class BeetrackCredentialsModel(db.Model):

    __tablename__ = "beetrack_credentials"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_key = db.Column(db.String(255))
    account_uuid = db.Column(db.String(255))
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))

    def __repr__(self):
        return 'Beetrack_credential ' + str(self.id)

    def __init__(self, api_key, account_uuid, shop_id_beetrack):
        self.api_key = api_key
        self.account_uuid = account_uuid
        self.shop_id_beetrack = shop_id_beetrack

    @property
    def serialize(self):
        return {'api_key': self.api_key}

    @classmethod
    def find_by_uuid(cls, account_uuid):
        return cls.query.filter_by(account_uuid= account_uuid).first()

    @classmethod
    def find_by_shop_id(cls, shop_id):
        return cls.query.filter_by(shop_id= shop_id).first()

    def save_to_db(self):
        print(self.shop_id_beetrack)
        db.session.add(self)
        db.session.commit()
