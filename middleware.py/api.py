import requests, json

# Dejar esots accesos deja muy expuesta la informacion de la base de datos. Evaluar eliminar caminos y utilizar
# solo los request del ORM.
class Api():

    def __init__(self):
        self.base_url = "http://localhost:5000"

    def get_shopify_credentials(self, account_uuid):
        url = self.base_url + "/beetrack_credentials/" + str(account_uuid)
        r = requests.get(url).json()
        return r

    def get_beetrack_credentials(self, user_name):
        url = self.base_url + "/shopify_credentials/" + str(user_name)
        r = requests.get(url).json()
        return r
