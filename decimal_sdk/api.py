import json

import requests
from requests import Response
from wallet import Wallet

"""
That's a stub
"""
from .transactions import Transaction


class DecimalAPI:
    """
    Base class to perform operations on Decimal API
    """
    def __init__(self, base_url: str):
        self.base_url = base_url
        if self.base_url[-1]:
            self.base_url += '/'

    def get_address(self, address: str):
        self.validate_address(address)
        return self.__request(f'address/{address}')

    def get_coin(self, name: str):
        # todo validate name?
        return self.__request(f'coin/{name}')

    def get_coins_list(self):
        return self.__request('coin')

    def get_multisig(self, address: str):
        self.validate_address(address)
        return self.__request(f'/multisig/{address}')

    def get_multisigs(self, address: str):
        self.validate_address(address)
        return self.__request(f'/address/{address}/multisigs')

    def get_my_transactions(self, wallet: Wallet):
        return self.__request(f'/address/${wallet.get_address()}/txs')

    def get_nonce(self, address: str):
        self.validate_address(address)
        return self.__request(f'/rpc/auth/accounts/{address}')

    def get_stakes(self, address: str):
        self.validate_address(address)
        return self.__request(f'/address/{address}/stakes')

    def get_tx(self):
        pass

    def get_txs_multisign(self):
        pass

    def get_validator(self, address: str):
        self.validate_address(address)
        return self.__request(f'/validator/{address}')

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
