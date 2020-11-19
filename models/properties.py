from db import db

class Properties():

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()