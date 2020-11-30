import requests

class BeetrackApiHandler:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Content-Type' : 'Applicaction/json',
            'X-AUTH-TOKEN' : self.api_key
            }
        self.base_url = 'https://app.beetrack.com/api/external/v1'

    def verify_apikey(self):
        url = self.base_url + "/trucks"
        r = requests.get(url, headers = self.headers)
        if r.status_code != 401:
            return True
        return False
    
    def get_dispatch(self, identifier):
        url = self.base_url + '/dispatches/' + identifier
        r = requests.get(url, headers = self.headers).json()
        return r

    def create_dispatch(self, data):
        url = self.base_url + "/dispatches"
        r = requests.post(url, headers = self.headers, json = data).json()
        return r 
