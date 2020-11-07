import json

import requests
from requests import Response


class DecimalAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_coins_list(self) -> dict:
        return self.__request('coin')

    def __request(self, path: str, method: str = 'get') -> dict:
        url = self.base_url + path
        if method == 'get':
            response = requests.get(url)
        else:
            response = requests.post(url)
        return self.__process_response(response)

    def __process_response(self, response: Response) -> dict:
        return json.loads(response.text)
