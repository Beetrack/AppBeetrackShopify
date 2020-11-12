from flask import Blueprint, session, redirect, Response
from configurations import Configurations as cfg

installation = Blueprint("install", __name__)

@installation.route('/install')
def install():
    if "shop" in session:
        shop = session["shop"]
        auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
            shop,
            cfg.SHOPIFY_CFG['API_KEY'],
            cfg.SHOPIFY_CFG['SCOPE'],
            cfg.SHOPIFY_CFG['REDIRECT_URI']
            )
        print(auth_url)
        return redirect(auth_url)
    else: 
        return Response(response="Error: Parameter shop Not Found", status= 500)