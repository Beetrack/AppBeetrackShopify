import requests, json
from configurations import Configurations as cfg

class ShopifyApiHandler:

    def __init__(self, shop):
        self.shop = shop
        self.base_url = 'https://{}/admin/api/2020-07/'.format(self.shop)

    def get_access_token(self, code):
        params = {
            "client_id" : cfg.SHOPIFY_CFG['API_KEY'],
            "client_secret" : cfg.SHOPIFY_CFG['API_SECRET'],
            "code" : code
            }
        url = "https://{0}/admin/oauth/access_token".format(self.shop)
        r = requests.post(url, data=params)
        resp_dict = json.loads(r.text)
        access_token = resp_dict.get("access_token")
        return access_token

    def create_webhook(self, api_key):
        headers = {
            'X-Shopify-Access-Token': api_key,
            'Content-Type': 'application/json'
        }
        #Dejar en variable de ambiente
        #"https://7mfmofytje.execute-api.us-west-2.amazonaws.com/staging/shopify_handler/integrate"
        params = {
            "webhook": {
                "topic": "orders/fulfilled",
                "address": "https://c3173cae7300aa5864da751d2ce20d1d.m.pipedream.net",
                "format": "json"
                }
            }
        url = self.base_url + 'webhooks.json'
        r = requests.post(url= url, headers= headers, json= params)
        if r.status_code == 201 or r.status_code == 422 :
            return True
        return False
