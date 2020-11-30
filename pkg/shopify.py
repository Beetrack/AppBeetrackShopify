import requests, json

class ShopifyApiHandler:

    def __init__(self):
        self.shop = "test-beetrack-shop.myshopify.com"
        self.api_key = "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"
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