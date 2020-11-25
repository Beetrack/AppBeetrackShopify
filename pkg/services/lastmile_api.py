import requests

class LastMileApi:

    def __init__(self):
        self.lastmile_url = "https://app.beetrack.com/api/external/v1"

    def create_dispatch(self, lastmile_api_key, data):
        lastmile_headers = {
            "X-AUTH-TOKEN": lastmile_api_key,
            "Content-Type": "application/json"
            }
        url = self.lastmile_url + "/dispatches"
        response = requests.post(url, headers = lastmile_headers, json = data).json()
        return response
