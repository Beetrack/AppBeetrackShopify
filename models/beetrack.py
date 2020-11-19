from db import db
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

    @event.listens_for(Beetrack, 'before_insert')
    def validate_api_key(self):
        r = requests.get('https://app.beetrack.com/api/external/v1/trucks', headers = {'Content-Type': 'application/json', 'X-AUTH-TOKEN': self.api_key})
        if r.status_code == 200:
            return True
        else:
            raise Exception('Invalid API Key')

    @classmethod
    def find_by_uuid(cls, account_uuid):
        return cls.query.filter_by(account_uuid = account_uuid).first()
