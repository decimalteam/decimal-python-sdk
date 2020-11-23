# from abc import ABC

from .wallet import Wallet

"""
That's a stub
"""


class Transaction:
    def __init__(self, **kwargs):
        pass

    def sign(self, private_key):
        pass

    def __generate_signature(self):
        pass

    def serialise(self):
        pass

    def _validate_params(self):
        pass


class BuyCoinTransaction(Transaction):
    def __init__(self, coin_to_buy, amount, coin_to_sell, **kwargs):
        self.coin_to_buy = coin_to_buy.upper()
        self.amount = amount
        self.coin_to_sell = coin_to_sell
        super().__init__(**kwargs)
