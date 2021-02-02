import json
import hashlib
import requests
import base64
import bech32

from Cryptodome.Hash import SHA256
import ethereum.transactions as crypto

from .types import FEES
from .wallet import Wallet
from .transactions import Transaction
from .utils.helpers import get_amount_uni
"""
That's a stub
"""


class DecimalAPI:
    """
    Base class to perform operations on Decimal API.
    Create new instance of api with passing base URL to DecimalAPI class.
    """
    unit = 0.001

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

        commission = self.__get_comission(tx, "del", FEES["coin/send_coin"])
        fee_amount = {"denom": "del", "value": commission["base"]}

        wallet.nonce = json.loads(self.get_nonce(wallet.get_address()))["result"]
        tx.signer.chain_id = self.get_chain_id()
        tx.signer.account_number = str(wallet.nonce["value"]["account_number"])
        tx.signer.sequence = str(wallet.nonce["value"]["sequence"])
        tx_data = tx.message.get_message()
        tx_data["fee"] = fee_amount
        tx.fee = fee_amount
        tx.sign(wallet)
        payload = {"tx": {}, "mode": "sync"}
        payload["tx"]["msg"] = [tx_data]
        payload["tx"]["memo"] = tx.memo
        payload["tx"]["signatures"] = []
        print("Payload: ")
        print(payload)

        for sig in tx.signatures:
            payload["tx"]["signatures"].append(sig.get_signature())

        print(payload)
        return self.__request(url, 'post', json.dumps(payload))

    def issue_check(self, wallet, data):
        new_data = {
            "coin": data["coin"].lower(),
            "amount": get_amount_uni(data["amount"]),
            "nonce": data["nonce"],
            "due_block": +data["due_block"],
            "passphrase": data["password"],
        }

        chain_id = self.get_chain_id()

        passphrase_hash = SHA256.new(new_data["passphrase"]).digest()
        passphrase_priv_key = passphrase_hash

        check_hash = self.__rpl_hash([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
        ])

        sig = crypto.ecsign(check_hash, passphrase_priv_key)
        self.set_signature(sig)


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
        if not coin["ok"]:
            raise Exception('Coin not found')
        coin = coin["result"]
        reserve = get_amount_uni(int(coin["reserve"]), True)
        supply = get_amount_uni(int(coin["volume"]), True)

        # if int(coin["crr"]) == 0:
        #     return 1

        crr = int(coin["crr"]) / 100

        if int(supply) < 1:
            amount = 1
        else:
            amount = int(supply)

        if int(supply) == 0:
            return 0

        result = amount / int(supply)
        result = 1 - result
        result = pow(result, 1 / crr)
        result = (1 - result) * reserve

        return result

    def __get_tx_size(self, tx: Transaction):
        preparedTx = {
            "type": 'cosmos-sdk/StdTx',
            "value":
                tx.message.get_message()
        }
        signatureSize = 109
        resp = json.loads(self.__request('rpc/txs/encode', 'post', json.dumps(preparedTx)))
        encoded_tx_base64 = resp["tx"]
        encoded_tx = len(base64.b64decode(encoded_tx_base64))
        size = encoded_tx + signatureSize
        return size

    def __get_comission(self, tx: Transaction, fee_coin, operation_fee):
        ticker = fee_coin
        text_size = self.__get_tx_size(tx)
        print("text size: ", text_size)
        print("operation fee", operation_fee)
        fee_for_text = text_size * 2
        fee_in_base = operation_fee + fee_for_text + 10

        if tx.message.get_type() == 'coin/multi_send_coin':
            number_of_participants = len(tx.message.get_value().sends)
            fee_for_participants = 5 * (number_of_participants - 1)
            fee_in_base = fee_in_base + fee_for_participants

        if fee_coin in ['del', 'tdel']:
            return {"coinPrice": "1", "value": fee_in_base, "base": fee_in_base}

        coin_price = self.__get_coin_price(ticker)
        fee_in_custom = fee_in_base / (coin_price / self.unit)
        return {"coinPrice": str(coin_price), 'value': fee_in_custom, 'base': fee_in_base}

    def __request(self, path: str, method: str = 'get', payload=None):
        url = (self.base_url + path).lower()
        if method == 'get':
            response = requests.get(url)
        else:
            response = requests.post(url, payload)
        return response.text
