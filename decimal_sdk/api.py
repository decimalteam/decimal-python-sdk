import json
import hashlib
import requests
import base58
from ecdsa import SigningKey, SECP256k1
import bech32
from mnemonic import Mnemonic

from .transactions import Transaction
from .wallet import Wallet
import pprint


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
        # comission = self.__get_comission(payload["tx"])
        payload["tx"]["fee"] = {"amount": [], "gas": 0}
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

    @staticmethod
    def __rpl_hash(data):
        return hashlib.sha3_256(data)

    def __get_chain_id(self):
        url = "rpc/node_info"
        resp = json.loads(self.__request(url))
        chain_id = resp["node_info"]["network"]
        return chain_id

    def __get_coin_price(self, name: str):
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
        fee = {
            "amount": [],
            "gas": "0"
        }
        return fee

    def __request(self, path: str, method: str = 'get', payload=None):
        url = (self.base_url + path).lower()
        print(url)
        if method == 'get':
            print(url)
            response = requests.get(url)
        else:
            response = requests.post(url, payload)
        return response.text

    def issue_check(self, wallet: Wallet, inc_data):
        chain_id = self.__get_chain_id()
        data = {
            "coin": inc_data["coin"].lower(),
            "amount": inc_data["amount"],
            "nonce": inc_data["nonce"],
            "due_block": inc_data["due_block"],
            "passphrase": inc_data["password"]
        }
        passphrase_hash = hashlib.sha256(data["passphrase"]).digest()
        passphrase_priv_key = passphrase_hash
        check_hash = self.__rpl_hash([
            chain_id,
            data["coin"],
            data["amount"],
            data["nonce"],
            data["due_block"],
        ])

        lock_obj = SigningKey.from_string(check_hash, passphrase_priv_key)
        lock_signature = []
        i = 0
        while i < 64:
            lock_signature[i] = lock_obj.privkey[i]
            i += 1

        lock_signature[64] = lock_obj # todo what is it recid

        check_locked_hash = self.__rpl_hash([
            chain_id,
            data["coin"],
            data["amount"],
            data["nonce"],
            data["due_block"],
            lock_signature
        ])

        check_obj = SigningKey.from_string(check_locked_hash, wallet.get_private_key())
        check = self.__rpl_hash([
            chain_id,
            data["coin"],
            data["amount"],
            data["nonce"],
            data["due_block"],
            lock_signature,
            check_obj.recid + 27, # todo what is recid
            check_obj.privkey[0:32],
            check_obj.privkey[32:64],
        ])

        return base58.b58encode(check)

    def redeem_check(self, data, wallet: Wallet):
        passphrase_hash = hashlib.sha256(data["passphrase"]).digest()
        passphrase_priv_key = passphrase_hash
        words = bech32.bech32_decode(wallet.get_address())
        # sender_address = self.__rpl_hash(bech32.)
