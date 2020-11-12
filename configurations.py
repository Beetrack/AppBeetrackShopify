import os

class Configurations():

    SECRET_KEY = os.environ.get('SECRET_KEY')
    HOST = "localhost:5000"
    
    
    SHOPIFY_CFG = {
        'API_KEY' : os.environ.get('API_KEY_SHOPIFY'),
        'API_SECRET' : os.environ.get('API_SECRET_SHOPIFY'),
        'APP_HOME' : 'http://' + HOST,
        'CALLBACK_URL' : 'http://' + HOST + '/install',
        'REDIRECT_URI' : 'http://' + HOST + '/connect',
        'SCOPE' : 'write_orders'
    }
    DB_CFG = {
        'DB_NAME' : os.environ.get('SHOPIFY_DB_NAME'),
        'DB_USER_NAME' : os.environ.get('SHOPIFY_DB_USER'),
        'DB_PASS' : os.environ.get('SHOPIFY_DB_PASS'),
        'DB_HOST' : os.environ.get('SHOPIFY_DB_HOST')
    }