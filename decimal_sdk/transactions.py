# from abc import ABC
import rlp
import sslcrypto
from Cryptodome.Hash import SHA256
from Cryptodome.Hash import keccak
from Cryptodome.Signature import DSS

from .wallet import Wallet

"""
That's a stub
"""


class Transaction:
    signature = ''
    GENERAL_TX_DATA = {
        'nonce': 0x0,
        'gas_limit': 0,
        'gas_amount': 0,
        'gas_coin': 'DEL',
        'chain_id': 0
    }

    def __init__(self, **kwargs):
        params = {
            'coin': kwargs['coin'],
            'to': kwargs['to'],
            'value': kwargs['value']
        }
        self.__body = {**self.GENERAL_TX_DATA, **params}

    def sign(self, private_key):
        self.signature = self.__rlp_tx_body()

    def __hash_tx_body(self):
        return keccak.new().update(self.__rlp_tx_body())

    def __rlp_tx_body(self):
        list_data = list(self.__body.values())

        return rlp.encode(list_data)

    def __generate_signature(self, private_key):
        # curve = sslcrypto.ecc.get_curve('secp256k1')
        # pub_key_len = curve._backend.public_key_length
        # signature = curve.sign(b'text', private_key, hash=None)
        # v = signature[0]
        # r = int.from_bytes(signature[1:pub_key_len + 1], byteorder='big')
        # s = int.from_bytes(signature[pub_key_len + 1:], byteorder='big')
        # signature = rlp.encode([v, r, s]).hex()
        # return signature
        pass

    def serialise(self):
        pass

    def _validate_params(self, **kwargs):
        pass


# class BuyCoinTransaction(Transaction):
#     def __init__(self, coin_to_buy, amount, coin_to_sell, **kwargs):
#         self.coin_to_buy = coin_to_buy.upper()
#         self.amount = amount
#         self.coin_to_sell = coin_to_sell
#         super().__init__(**kwargs)


# class SellCoinTransaction(Transaction):
#     def __init__(self, coin_to_buy, amount, coin_to_sell):
#         pass
#
#
# class CreateCoinTransaction(Transaction):
#     def __init__(self, coin_name, ticker, initial_supply, max_supply, reserve, crr):
#         pass


class SendCoinTransaction(Transaction):
    def __init__(self, to, coin, value):
        super().__init__(to=to, coin=coin, value=value)


class DeclareCandidateTransaction(Transaction):
    def __init__(self):
        pass


class DelegateTransaction(Transaction):
    def __init__(self, address, coin, stake):
        pass


class UnbondTransaction(Transaction):
    pass


class SetOnlineTransaction(Transaction):
    pass


class SetOfflineTransaction(Transaction):
    pass


class EditCandidate(Transaction):
    pass
