import json

import requests
# from requests import Response
from .transactions import Transaction
from .wallet import Wallet
import pprint
import json

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

    def get_tx(self, tx_hash: str):
        if len(tx_hash) < 1:
            raise Exception('Hash is empty')
        return self.__request("rpc/tx", "get", '{ "params": { "hash": "0x$' + tx_hash + '"}}')

    def get_txs_multisign(self, address: str, limit: int = 1, offset: int = 0):
        self.validate_address(address)
        return self.__request(f"/multisig/${address}/txs")

    def get_validator(self, address: str):
        self.validate_address(address)
        return self.__request(f'/validator/{address}')

    def send_tx(self, tx: Transaction, wallet: Wallet):
        """Method to sign and send prepared transaction"""
        url = "rpc/txs"
        tx_data = tx.message.get_message()
        tx.sign(wallet)
        payload = {"tx": {}, "mode": "sync"}
        payload["tx"]["msg"] = [tx_data]
        payload["tx"]["memo"] = tx.memo
        payload["tx"]["signatures"] = []
        comission = self.__get_comission(payload["tx"])
        payload["tx"]["fee"] = {"amount": [], "gas": comission}
        for sig in tx.signatures:
            payload["tx"]["signatures"].append(sig.get_signature())
            print(sig.get_signature())
        print(json.dumps(payload))
        # print(payload)
        return self.__request(url, 'post', json.dumps(payload))

    @staticmethod
    def validate_address(address: str):
        if len(address) != 41 or not address.startswith('dx'):
            raise Exception('Invalid address')

    def get_coin_price(self, name: str):
        coin = json.loads(self.get_coin(name))
        if not coin:
            raise Exception('Coin not found')
        reserve = coin["reserve"]
        supply = coin["volume"]
        crr = coin["crr"] / 100;

        if supply < 1:
            amount = 1
        else:
            amount = supply

        if supply == 0:
            return 0

        return 1 - (((1 - (amount / supply)) / crr) * reserve)

    def __get_tx_size(self, tx):
        signatureSize = 109
        preparedTx = {
            "type": 'cosmos-sdk/StdTx',
            "value": {
                tx
            }
        }
        resp = json.loads(self.__request('/rpc/txs/encode', 'post', preparedTx))
        encoded_tx_base64 = resp["tx"]
        size = ((len(encoded_tx_base64) * 3) / 4) - signatureSize
        return size

    def __get_comission(self, tx):
        msg_size = self.__get_tx_size(tx)

    def __request(self, path: str, method: str = 'get', payload=None):
        url = (self.base_url + path).lower()
        print(url)
        if method == 'get':
            print(url)
            response = requests.get(url)
        else:
            response = requests.post(url, payload)
        return response.text