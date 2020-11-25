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


class SellCoinTransaction(Transaction):
    def __init__(self, coin_to_buy, amount, coin_to_sell):
        pass


class CreateCoinTransaction(Transaction):
    def __init__(self, coin_name, ticker, initial_supply, max_supply, reserve, crr):
        pass


class SendCoinTransaction(Transaction):
    def __init__(self, recipient, coin_to_send, amount):
        pass


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
