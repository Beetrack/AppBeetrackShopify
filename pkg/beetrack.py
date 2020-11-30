import requests, json, ipdb

class BeetrackApiHandler:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Content-Type' : 'application/json',
            'X-AUTH-TOKEN' : self.api_key
            }
        self.base_url = 'https://app.beetrack.com/api/external/v1'

    def get_dispatch(self, identifier):
        url = self.base_url + '/dispatches/' + identifier
        r = requests.get(url, headers = self.headers).json()
        return r

    def create_dispatch(self, data):
        url = self.base_url + "/dispatches"
        ipdb.set_trace()
        r = requests.post(url, headers = self.headers, json = data).json()
        return r