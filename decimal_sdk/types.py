import base64
import json
from hashlib import sha256

from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_string_canonize

from decimal_sdk import Wallet
from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.utils import beautify_json


class Coin:
    denom: str
    amount: str

    def __init__(self, denom: str, amount: str):
        self.denom = denom
        self.amount = amount

    def __dict__(self):
        return {'denom': self.denom, 'amount': self.amount}


class Signature:
    pub_key: str
    signature: str

    def __init__(self, signature: str, pub_key: str):
        self.signature = signature
        self.pub_key = pub_key

    def __dict__(self):
        return {'pub_key': {'type': 'tendermint/PubKeySecp256k1', 'value': self.pub_key},
                'signature': self.signature}


class Fee:
    amount: [Coin]
    gas: str

    def __init__(self, amount: [Coin], gas: str):
        self.amount = amount
        self.gas = gas

    def __dict__(self):
        return {'gas': self.gas, 'amount': [coin.__dict__() for coin in self.amount]}


class SignMeta:
    account_number: str
    chain_id: str
    sequence: str

    def __init__(self, account_number: str = '18', chain_id: str = 'decimal-devnet-11-20-18-00', sequence: str = '7'):
        self.account_number = account_number
        self.chain_id = chain_id
        self.sequence = sequence


class StdSignMsg:
    # Tx part
    fee: Fee
    memo: str
    msgs: [BaseMsg]
    # Meta part
    account_number: str
    chain_id: str
    sequence: str

    signatures: [Signature] = []

    def __init__(self, tx, meta: SignMeta):
        self.fee = tx.fee
        self.msgs = tx.msgs
        self.memo = tx.memo

        self.account_number = meta.account_number
        self.chain_id = meta.chain_id
        self.sequence = meta.sequence

    def add_msg(self, msg: BaseMsg):
        self.msgs.append(msg)

    def sign(self, wallet: Wallet):
        private_key = wallet.get_private_key()
        pub_key = wallet.get_public_key()
        sig = self.__generate_signature(private_key)
        self.signatures.append(Signature(signature=sig, pub_key=pub_key))

    def __get_body_bytes(self):
        data = beautify_json(
            {'fee': self.fee.__dict__(), 'memo': self.memo, 'msgs': [msg.__dict__() for msg in self.msgs],
             'account_number': self.account_number, 'chain_id': self.chain_id, 'sequence': self.sequence})

        return json.dumps(data, separators=(',', ':'), ).encode('utf-8')

    def __generate_signature(self, private_key):
        data = self.__get_body_bytes()
        hash_ = sha256(data).digest()
        sk = SigningKey.from_string(private_key, curve=SECP256k1)

        signature = sk.sign_digest_deterministic(hash_, hashfunc=sha256, sigencode=sigencode_string_canonize)

        base_signature = base64.b64encode(signature)

        return base_signature.decode('utf-8')

    def __dict__(self):
        return {'fee': self.fee.__dict__(), 'memo': self.memo, 'msgs': [msg.__dict__() for msg in self.msgs],
                'account_number': self.account_number, 'chain_id': self.chain_id, 'sequence': self.sequence,
                'signatures': [sig.__dict__() for sig in self.signatures]}
