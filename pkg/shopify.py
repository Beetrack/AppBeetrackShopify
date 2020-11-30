import requests, json

class ShopifyApiHandler:

    def __init__(self, shop, shopify_api_key):
        self.shop = shop
        self.api_key = shopify_api_key
        self.base_url = 'https://{}/admin/api/2020-10'.format(self.shop)
        self.headers = {
            'X-Shopify-Access-Token': self.api_key,
            'Content-Type': 'application/json'
        }

    def create_note_order(self, order_id, payload):
        url = self.base_url + '/orders/{}.json'.format(order_id)
        r = requests.put(url= url, headers= self.headers, json = payload).json()
        print(r)
        return r

    def create_fulfillment(self, order_id, fulfillment_id, payload):
        url = self.base_url + '/orders/{}/fulfillments/{}.json'.format(order_id, fulfillment_id)
        r = requests.put(url= url, headers= self.headers, json = payload).json()
        print(r)
        return r