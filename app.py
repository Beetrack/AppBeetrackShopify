from db import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from configurations import Configurations as cfg

from resources.beetrack import Beetrack
from resources.shopify import Shopify

from views.configuration import configuration
from views.install import installation
from views.connect import connection
from views.webhooks import webhooks

app = Flask(__name__)
app.secret_key = cfg.SECRET_KEY
app.register_blueprint(configuration)
app.register_blueprint(installation)
app.register_blueprint(connection)
app.register_blueprint(webhooks)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
    cfg.DB_CFG['DB_USER_NAME'], cfg.DB_CFG['DB_PASS'], cfg.DB_CFG['DB_HOST'], cfg.DB_CFG['DB_NAME'])

api = Api(app)
api.add_resource(Shopify, '/shopify_credentials/<string:user_name>')
api.add_resource(Beetrack, '/beetrack_credentials/<string:account_uuid>')

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug= True, port= 5000)
