
class Configuration():
    SECRET_KEY = "scdnodasv6d5f4v6a5d1fv6adf1v6sdfb65df4"
    HOST = "localhost:5000"

    SHOPIFY_CONFIGURATION = {
        'API_KEY' : 'aca387d70f950f917a874ad0cb0fe75c',
        'API_SECRET' : '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',
        'APP_HOME' : 'http://' + HOST,
        'CALLBACK_URL' : 'http://' + HOST + '/home/install',
        'REDIRECT_URI' : 'http://' + HOST + '/connect',
        'SCOPE' : 'write_products'
    }