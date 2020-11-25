# from abc import ABC

from .wallet import Wallet

"""
That's a stub
"""


class Transaction:
    signature = ''

    def __init__(self, **kwargs):
        self._validate_params(**kwargs)
        self._value = kwargs

    def sign(self, private_key):
        pass

    def __generate_signature(self):
        pass

    def serialise(self):
        pass

    def _validate_params(self, **kwargs):
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
        super().__init__(recipient=recipient, coin_to_send=coin_to_send, amount=amount)


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
