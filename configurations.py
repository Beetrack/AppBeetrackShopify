import os

class Configurations():

    SECRET_KEY = "1234abcd"
    HOST = "localhost:5000"

    SHOPIFY_CFG = {
        'API_KEY' : "9d4b7691f204f97e02489042392fb373",
        'API_SECRET' : "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",
        'APP_HOME' : 'http://' + HOST,
        'CALLBACK_URL' : 'http://' + HOST + '/install',
        'REDIRECT_URI' : 'http://' + HOST + '/connect',
        'SCOPE' : 'write_orders'
    }

    DB_CFG = {
        'DB_NAME' : "beetrack-shopify-db",
        'DB_USER_NAME' : "bianca",
        'DB_PASS' : "123456",
        'DB_HOST' : "localhost"
    }