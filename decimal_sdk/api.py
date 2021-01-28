import json
import hashlib
import requests
import base64

from .types import FEES
from .wallet import Wallet


"""
That's a stub
"""
from .transactions import Transaction


class DecimalAPI:
    unit = 0.001
    """
    Base class to perform operations on Decimal API
    """
    def __init__(self, base_url: str):
        self.base_url = base_url
        if self.base_url[-1]:
            self.base_url += '/'

    def get_address(self, address: str):
        self.__validate_address(address)
        return self.__request(f'address/{address}')

    def get_coin(self, name: str):
        return self.__request(f'coin/{name}')

    def get_coins_list(self):
        return self.__request('coin')

    def get_multisig(self, address: str):
        self.__validate_address(address)
        return self.__request(f'multisig/{address}')

    def get_multisigs(self, address: str):
        self.__validate_address(address)
        return self.__request(f'address/{address}/multisigs')

    def get_my_transactions(self, wallet: Wallet):
        return self.__request(f'address/${wallet.get_address()}/txs')

    def get_nonce(self, address: str):
        self.__validate_address(address)
        return self.__request(f'rpc/auth/accounts/{address}')

    def get_stakes(self, address: str):
        self.__validate_address(address)
        return self.__request(f'address/{address}/stakes')

    def get_tx(self, tx_hash: str):
        if len(tx_hash) < 1:
            raise Exception('Hash is empty')
        return self.__request("rpc/tx", "get", '{ "params": { "hash": "0x$' + tx_hash + '"}}')

    def get_txs_multisign(self, address: str, limit: int = 1, offset: int = 0):
        self.__validate_address(address)
        return self.__request(f"multisig/${address}/txs")

    def get_validator(self, address: str):
        self.__validate_address(address)
        return self.__request(f'validator/{address}')

    def send_tx(self, tx: Transaction, wallet: Wallet):
        """Method to sign and send prepared transaction"""

        url = "rpc/txs"
        wallet.nonce = json.loads(self.get_nonce(wallet.get_address()))["result"]
        tx.signer.chain_id = self.get_chain_id()
        tx.signer.account_number = str(wallet.nonce["value"]["account_number"])
        tx.signer.sequence = str(wallet.nonce["value"]["sequence"])
        tx_data = tx.message.get_message()
        tx.sign(wallet)
        payload = {"tx": {}, "mode": "sync"}
        payload["tx"]["msg"] = [tx_data]
        payload["tx"]["memo"] = tx.memo
        payload["tx"]["signatures"] = []

        comission = self.__get_comission(tx, "del", FEES["coin/send_coin"])
        fee_amount = {"denom": "del", "value": comission["base"]}
        # TODO: enable tx fee calc
        # payload["tx"]["fee"] = {"amount": [], "gas": "0"}
        payload["tx"]["fee"] = {"amount": [fee_amount], "gas": "0"}

        for sig in tx.signatures:
            payload["tx"]["signatures"].append(sig.get_signature())

        print(payload)
        return self.__request(url, 'post', json.dumps(payload))

    def get_chain_id(self):
        url = "rpc/node_info"
        resp = json.loads(self.__request(url))
        chain_id = resp["node_info"]["network"]
        return chain_id

    @staticmethod
    def __validate_address(address: str):
        if len(address) < 41 or not address.startswith('dx'):
            raise Exception('Invalid address')

    @staticmethod
    def __rpl_hash(data):
        return hashlib.sha3_256(data)

    def __get_coin_price(self, name: str):
        coin = json.loads(self.get_coin(name))
        print(coin)
        if not coin["ok"]:
            raise Exception('Coin not found')
        coin = coin["result"]
        reserve = int(coin["reserve"])
        supply = coin["volume"]

        if int(coin["crr"]) == 0:
            return 1

        crr = int(coin["crr"]) / 100

        if int(supply) == 0:
            return 0

        if int(supply) < 1:
            amount = 1
        else:
            amount = int(supply)

        result = amount / int(supply)
        result = 1 - result
        result = pow(result, 1 / crr)
        result = (1 - result) * reserve

        return result

    def __get_tx_size(self, tx: Transaction):
        signatureSize = 109
        preparedTx = {
            "type": 'cosmos-sdk/StdTx',
            "value":
                tx.message.get_message()
        }
        resp = json.loads(self.__request('rpc/txs/encode', 'post', json.dumps(preparedTx)))
        encoded_tx_base64 = resp["tx"]
        decoded = int.from_bytes(base64.b64decode(encoded_tx_base64), 'big')
        size = decoded + signatureSize
        return size

    def __get_comission(self, tx: Transaction, fee_coin, operation_fee):
        ticker = fee_coin
        text_size = self.__get_tx_size(tx)
        fee_for_text = text_size * 2
        fee_in_base = operation_fee + fee_for_text + 10

        if tx.message.get_type() == 'coin/multi_send_coin':
            number_of_participants = len(tx.message.get_value().sends)
            fee_for_participants = 5 * (number_of_participants - 1)
            fee_in_base = fee_in_base + fee_for_participants

        if fee_coin in ['del', 'tdel']:
            # print({'coinPrice': '1', 'value': fee_in_base, 'base': fee_in_base})
            return {'coinPrice': '1', 'value': fee_in_base, 'base': fee_in_base}

        coin_price = self.__get_coin_price(ticker)
        fee_in_custom = fee_in_base / (coin_price / self.unit)
        # print({"coinPrice": str(coin_price), 'value': fee_in_custom, 'base': fee_in_base})
        return {"coinPrice": str(coin_price), 'value': fee_in_custom, 'base': fee_in_base}

    def __request(self, path: str, method: str = 'get', payload=None):
        url = (self.base_url + path).lower()
        if method == 'get':
            response = requests.get(url)
        else:
            response = requests.post(url, payload)
        return response.text
