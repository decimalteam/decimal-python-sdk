import json
import rlp
import requests
import base64
import base58
import bech32
import sha3

from hashlib import sha256
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_string_canonize

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
        print(json.dumps(payload))

        for sig in tx.signatures:
            payload["tx"]["signatures"].append(sig.get_signature())

        print(json.dumps(payload))
        return self.__request(url, 'post', json.dumps(payload))

    def issue_check(self, wallet, data):
        new_data = {
            "coin": data["coin"].lower(),
            "amount": int(get_amount_uni(int(data["amount"]), False)),
            "nonce": data["nonce"],
            "due_block": int(data["due_block"]),
            "passphrase": data["password"],
        }

        chain_id = self.get_chain_id()

        print('chain_id ', chain_id)

        passphrase_hash = SHA256.new(str.encode(new_data["passphrase"])).digest()
        pp = []
        for b in passphrase_hash:
            pp.append(b)
        print("passphrase_hash ", pp)

        check_hash = self.__rpl_hash([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
        ])

        ch = []
        for b in check_hash:
            ch.append(b)
        print("check_hash ", ch)

        passphrase_hash = sha256(str.encode(new_data["passphrase"])).digest()

        sk = SigningKey.from_string(passphrase_hash, curve=SECP256k1)
        lock_obj = sk.sign_digest_deterministic(check_hash, hashfunc=sha256, sigencode=sigencode_string_canonize)

        bts2 = []
        for b in lock_obj:
            bts2.append(b)
        lock_signature = bytearray(65)

        i = 0
        while i<64:
            lock_signature[i] = lock_obj[i]
            i += 1

        v, r, s = crypto.ecsign(check_hash, passphrase_hash)
        lock_signature[64] = v-27
        print("lock_signature ", lock_signature)

        check_locked_hash = self.__rpl_hash([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
            lock_signature
        ])
        clh = []
        for b in check_locked_hash:
            clh.append(b)
        print("check_locked_hash ", clh)
        pk = []
        for b in wallet.get_private_key():
            pk.append(b)
        print("pk ", pk)
        sk = SigningKey.from_string(wallet.get_private_key(), curve=SECP256k1)
        check_obj = sk.sign_digest_deterministic(check_locked_hash, hashfunc=sha256, sigencode=sigencode_string_canonize)
        co = []
        for b in check_obj:
            co.append(b)
        print("check_obj ", co)
        v, r, s = crypto.ecsign(check_locked_hash, wallet.get_private_key())

        rr = bytearray(32)
        ss = bytearray(32)

        i = 0
        while i < 32:
            rr[i] = crypto.int_to_32bytearray(r)[i]
            i += 1

        i = 0
        while i < 32:
            ss[i] = crypto.int_to_32bytearray(s)[i]
            i += 1

        print("___________")
        print([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
            lock_signature,
            v,
            rr,
            ss,
        ])
        print("___________")

        check = rlp.encode([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
            lock_signature,
            v,
            rr,
            ss,
        ])
        chk = []
        for b in check:
            chk.append(b)
        print("check", chk)
        return base58.b58encode(check)

    def redeem_check(self, data, wallet):
        passphrase_hash = SHA256.new(str.encode(data["password"])).digest()

        words = bech32.bech32_decode(wallet.get_address())
        print('words ', words)

        sender_address_hash = self.__rpl_hash(bech32.bech32_hrp_expand())
        sk = SigningKey.from_string(passphrase_hash, curve=SECP256k1)
        proof_obj = sk.sign_digest_deterministic(sender_address_hash, hashfunc=sha256, sigencode=sigencode_string_canonize)

        proof_signature = bytearray(65)

        i = 0
        while i<64:
            proof_signature[i] = proof_obj[i]
            i += 1

        v, r, s = crypto.ecsign(sender_address_hash, passphrase_hash)
        proof_signature[64] = v - 27

        proof = proof_signature

        return {
            "sender": wallet.get_address(),
            "check": data["check"],
            "proof": proof
        }

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
        khash = sha3.keccak_256()
        dt = rlp.encode(data)
        khash.update(dt)
        return khash.digest()

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
            number_of_participants = len(tx.message.get_message()["value"]["sends"])
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
import json
import rlp
import requests
import base64
import base58
import bech32
import sha3

from hashlib import sha256
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_string_canonize

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
        print(json.dumps(payload))

        for sig in tx.signatures:
            payload["tx"]["signatures"].append(sig.get_signature())

        print(json.dumps(payload))
        return self.__request(url, 'post', json.dumps(payload))

    def issue_check(self, wallet, data):
        new_data = {
            "coin": data["coin"].lower(),
            "amount": int(get_amount_uni(int(data["amount"]), False)),
            "nonce": data["nonce"],
            "due_block": int(data["due_block"]),
            "passphrase": data["password"],
        }

        chain_id = self.get_chain_id()

        print('chain_id ', chain_id)

        passphrase_hash = SHA256.new(str.encode(new_data["passphrase"])).digest()
        pp = []
        for b in passphrase_hash:
            pp.append(b)
        print("passphrase_hash ", pp)

        check_hash = self.__rpl_hash([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
        ])

        ch = []
        for b in check_hash:
            ch.append(b)
        print("check_hash ", ch)

        passphrase_hash = sha256(str.encode(new_data["passphrase"])).digest()

        sk = SigningKey.from_string(passphrase_hash, curve=SECP256k1)
        lock_obj = sk.sign_digest_deterministic(check_hash, hashfunc=sha256, sigencode=sigencode_string_canonize)

        bts2 = []
        for b in lock_obj:
            bts2.append(b)
        lock_signature = bytearray(65)

        i = 0
        while i<64:
            lock_signature[i] = lock_obj[i]
            i += 1

        v, r, s = crypto.ecsign(check_hash, passphrase_hash)
        lock_signature[64] = v-27
        print("lock_signature ", lock_signature)

        check_locked_hash = self.__rpl_hash([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
            lock_signature
        ])
        clh = []
        for b in check_locked_hash:
            clh.append(b)
        print("check_locked_hash ", clh)
        pk = []
        for b in wallet.get_private_key():
            pk.append(b)
        print("pk ", pk)
        sk = SigningKey.from_string(wallet.get_private_key(), curve=SECP256k1)
        check_obj = sk.sign_digest_deterministic(check_locked_hash, hashfunc=sha256, sigencode=sigencode_string_canonize)
        co = []
        for b in check_obj:
            co.append(b)
        print("check_obj ", co)
        v, r, s = crypto.ecsign(check_locked_hash, wallet.get_private_key())

        rr = bytearray(32)
        ss = bytearray(32)

        i = 0
        while i < 32:
            rr[i] = crypto.int_to_32bytearray(r)[i]
            i += 1

        i = 0
        while i < 32:
            ss[i] = crypto.int_to_32bytearray(s)[i]
            i += 1

        print("___________")
        print([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
            lock_signature,
            v,
            rr,
            ss,
        ])
        print("___________")

        check = rlp.encode([
            chain_id,
            new_data["coin"],
            new_data["amount"],
            new_data["nonce"],
            new_data["due_block"],
            lock_signature,
            v,
            rr,
            ss,
        ])
        chk = []
        for b in check:
            chk.append(b)
        print("check", chk)
        return base58.b58encode(check)

    def redeem_check(self, data, wallet):
        passphrase_hash = SHA256.new(str.encode(data["password"])).digest()

        words = bech32.bech32_decode(wallet.get_address())
        print('words ', words)

        sender_address_hash = self.__rpl_hash(bech32.bech32_hrp_expand())
        sk = SigningKey.from_string(passphrase_hash, curve=SECP256k1)
        proof_obj = sk.sign_digest_deterministic(sender_address_hash, hashfunc=sha256, sigencode=sigencode_string_canonize)

        proof_signature = bytearray(65)

        i = 0
        while i<64:
            proof_signature[i] = proof_obj[i]
            i += 1

        v, r, s = crypto.ecsign(sender_address_hash, passphrase_hash)
        proof_signature[64] = v - 27

        proof = proof_signature

        return {
            "sender": wallet.get_address(),
            "check": data["check"],
            "proof": proof
        }

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
        khash = sha3.keccak_256()
        dt = rlp.encode(data)
        khash.update(dt)
        return khash.digest()

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
            number_of_participants = len(tx.message.get_message()["value"]["sends"])
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
