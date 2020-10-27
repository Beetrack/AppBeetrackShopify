class Config(object):
    SECRET_KEY = 'HOLABIANCA'
    HOST = 'acac0b1e4aa6.ngrok.io'

    SHOPIFY_CONFIG = {
        "API_KEY" : '9d4b7691f204f97e02489042392fb373',
        'API_SECRET' : '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',
        'APP_HOME' : 'http://' + HOST,
        'CALLBACK_URL' : 'http://' + HOST + '/install',
        'REDIRECT_URI': 'http://' + HOST + '/connect',
        'SCOPE': 'write_orders'
    }