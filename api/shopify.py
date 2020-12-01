import requests, json
from configurations import Configurations as cfg

class ShopifyApiHandler:

    def __init__(self, shop, shopify_api_key):
        self.shop = shop
        self.api_key = shopify_api_key
        self.headers = {
            'X-Shopify-Access-Token': self.api_key,
            'Content-Type': 'application/json'
        }
        self.base_url = 'https://{}/admin/api/2020-10'.format(self.shop)

    def create_webhook(self):
        #leave endpoint in enviroment varible
        params = {
            "webhook": {
                "topic": "orders/fulfilled",
                "address": "https://7mfmofytje.execute-api.us-west-2.amazonaws.com/staging/shopify_handler/integrate",
                "format": "json"
                }
            }
        url = self.base_url + '/webhooks.json'
        r = requests.post(url = url, headers = self.headers, json = params)
        if r.status_code == 201 or r.status_code == 422 :
            return True
        return False

    def create_note_order(self, order_id, payload):
        url = self.base_url + '/orders/{}.json'.format(order_id)
        r = requests.put(url = url, headers = self.headers, json = payload).json()
        print(r)
        return r

    def create_fulfillment(self, order_id, fulfillment_id, payload):
        url = self.base_url + '/orders/{}/fulfillments/{}.json'.format(order_id, fulfillment_id)
        r = requests.put(url= url, headers= self.headers, json = payload).json()
        print(r)
        return r
    
class ShopifyToken:

    def __init__(self, shop):
        self.shop = shop

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

