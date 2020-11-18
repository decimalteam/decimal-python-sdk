import json

import requests
from requests import Response

from transaction import Transaction


class DecimalAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
        if self.base_url[-1]:
            self.base_url += '/'

    def get_coins_list(self):
        return self.__request('coin')

    def get_coin(self, name: str):
        return self.__request(f'coin/{name}')

    def get_address(self, address: str):
        self.validate_address(address)
        return self.__request(f'address/{address}')

    def get_stakes_by_address(self, address: str):
        self.validate_address(address)
        return self.__request(f'address/{address}/stakes')

    def send_tx(self, tx: Transaction):
        return self.__request('', 'post', tx)

    @staticmethod
    def validate_address(address: str):
        if len(address) != 41 or not address.startswith('dx'):
            raise Exception('Invalid address')

    def __request(self, path: str, method: str = 'get', payload=None):
        url = self.base_url + path
        if method == 'get':
            response = requests.get(url)
        else:
            response = requests.post(url, payload)
        return response.text
