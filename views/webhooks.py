from flask import Blueprint, session, redirect, render_template
from api.shopify import ShopifyApiHandler

webhooks = Blueprint('webhooks', __name__)

@webhooks.route('/webhooks')
def webhooks_shopify():
    if 'shop' and 'shopify_token' in session:
        shop = session["shop"]
        shopify_token = session['shopify_token']
        create_shopify_webhook = ShopifyApiHandler(shop).create_webhook(shopify_token)
        if create_shopify_webhook:
            account_uuid_info = session['account_uuid']
            return render_template('connected.html', content= account_uuid_info)
        else:
            return render_template('error.html')
    else:
        return redirect('/connect')
