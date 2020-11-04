import requests, json
import configurations as cfg

class ShopifyApiHandler:

    def get_access_token(self, shop, code):
        params = {
            "client_id" : cfg.SHOPIFY_CFG['API_KEY'],
            "client_secret" : cfg.SHOPIFY_CFG['API_SECRET'],
            "code" : code
            }
        r = requests.post("https://{0}/admin/oauth/access_token".format(shop), data=params)
        resp_dict = json.loads(r.text)
        access_token = resp_dict.get("access_token")
        
        return access_token