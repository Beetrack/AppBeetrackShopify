import requests

class BeetrackApiHandler:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Content-Type' : 'Applicaction/json',
            'X-AUTH-TOKEN' : self.api_key
            }
        self.url = 'https://app.beetrack.com/api/external/v1/trucks'

    def verify_apikey(self):
        r = requests.get(self.url, headers = self.headers)
        if r.status_code != 401:
            return True
        return False
