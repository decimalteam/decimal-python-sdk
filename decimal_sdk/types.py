import base64
import codecs
import json
from hashlib import sha256, sha3_256

import base58
import rlp
import secp256k1
from rlp.sedes import text, List, CountableList
import sslcrypto
from Cryptodome.Hash import keccak
from ecdsa import ecdsa, SigningKey, SECP256k1
from ecdsa.util import sigencode_der, sigencode_strings_canonize, sigencode_string_canonize

from decimal_sdk.msgs import SendCoinMsgValue
from decimal_sdk.tx_types import COIN_SEND


class BaseMsgValue(rlp.Serializable):
    pass


class Coin(rlp.Serializable):
    denom: str
    amount: str

    fields = [
        ('denom', text),
        ('amount', text)
    ]

    def __dict__(self):
        return {'denom': self.denom, 'amount': self.amount}


class Msg(rlp.Serializable):
    type: str
    value: SendCoinMsgValue

    fields = [
        ('type', text),
        ('value', SendCoinMsgValue)
    ]

    def __dict__(self):
        return {'type': self.type, 'value': self.value.__dict__()}


class Signature(rlp.Serializable):
    private_key: str
    signature: str

    fields = [
        ('private_key', text),
        ('signature', text)
    ]

    def __dict__(self):
        return {'pub_key': {'type': 'tendermint/PubKeySecp256k1', 'value': self.private_key},
                'signature': self.signature}


class Fee(rlp.Serializable):
    amount: [Coin]
    gas: str

    fields = [
        ('amount', CountableList([Coin])),
        ('gas', text)
    ]

    def __dict__(self):
        return {'gas': self.gas, 'amount': [coin.__dict__() for coin in self.amount]}


class SignMeta:
    account_number: str
    chain_id: str
    sequence: str

    def __init__(self, account_number: str, chain_id: str, sequence: str):
        self.account_number = account_number
        self.chain_id = chain_id
        self.sequence = sequence


class Tx:
    fee: Fee
    memo: str
    msg: [Msg]

    def __init__(self, msg: [Msg], fee: Fee = None, memo: str = ''):
        if fee is None:
            # TODO: Calculate fee
            fee = Fee([], '0')
        self.fee = fee
        self.memo = memo
        self.msg = msg


class StdSignMsg(rlp.Serializable):
    # Tx part
    fee: Fee
    memo: str
    msg: [Msg]
    # Meta part
    account_number: str
    chain_id: str
    sequence: str

    signatures: [Signature] = []

    fields = [
        ('fee', Fee),
        ('memo', text),
        ('msg', CountableList(Msg)),

        ('account_number', text),
        ('chain_id', text),
        ('sequence', text),

        ('signatures', CountableList(Signature))
    ]

    def sign(self, private_key):
        self.signatures.append(self.__generate_signature(private_key))

    # def __hash_tx_body(self):
    #     return keccak.new(digest_bits=512).update(self.__rlp_tx_body()).digest()

    def __rlp_tx_body(self):
        data = beautify_json(self.__dict__())

        return json.dumps(data, separators=(',', ':'))

    def __generate_signature(self, private_key):
        data = self.__rlp_tx_body()
        hash_ = sha256(data.encode('utf-8')).digest()
        sk = SigningKey.from_string(private_key, curve=SECP256k1)

        signature = sk.sign_digest_deterministic(hash_, hashfunc=sha256, sigencode=sigencode_string_canonize)

        base_signature = base64.b64encode(signature)

        return base_signature.decode('utf-8')

    def __dict__(self):
        return {'fee': self.fee.__dict__(), 'memo': self.memo, 'msgs': [msg.__dict__() for msg in self.msg],
                'account_number': self.account_number, 'chain_id': self.chain_id, 'sequence': self.sequence}


def beautify_json(value):
    if type(value) == list:
        return [beautify_json(elem) for elem in value]
    elif type(value) == dict:
        keys = list(value.keys())
        keys.sort()
        return {key: beautify_json(value[key]) for key in keys}
    else:
        return value


class SendCoinTx(Tx):
    def __init__(self, sender: str, to: str, coin: Coin, fee: Fee = None, memo: str = ''):
        super().__init__(msg=[Msg(type=COIN_SEND, value=SendCoinMsgValue(sender=sender, receiver=to, coin=coin))],
                         fee=fee, memo=memo)


def create_std_sign_tx(tx: Tx, meta: SignMeta):
    return StdSignMsg(
        fee=tx.fee,
        memo=tx.memo,
        msg=tx.msg,

        account_number=meta.account_number,
        chain_id=meta.chain_id,
        sequence=meta.sequence,

        signatures=[]
    )
