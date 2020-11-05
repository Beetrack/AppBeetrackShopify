import requests, json, sys
sys.path.insert(1, '/Users/adipr/OneDrive/Documentos/Python/BeeTrack/Integrations/Shopify/AppBeetrackShopify')

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
        r = requests.post("https://{0}/admin/oauth/access_token".format(self.shop), data=params)
        resp_dict = json.loads(r.text)
        access_token = resp_dict.get("access_token")
        
        return access_token

    def create_webhook(self, api_key):
        headers = {
            'X-Shopify-Access-Token': api_key,
            'Content-Type': 'application/json'
        }
        params = {
            "webhook": {
                "topic": "orders/fulfilled",
                "address": "https://7mfmofytje.execute-api.us-west-2.amazonaws.com/staging/shopify_handler/integrate",
                "format": "json"
                }
            }
        url = self.base_url + 'webhooks.json'
        print(url)
        r = requests.post(url= url, headers= headers, json= params)
        print(r.json())
        print(r.status_code)
        print(headers)
        print(params)
        print(api_key)
        if r.status_code == 201:
            return True
        return False
