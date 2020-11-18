from wallet import Wallet


class Transaction:
    def __init__(self, **kwargs):
        pass


class BuyCoinTransaction(Transaction):
    def __init__(self, coin_to_buy, amount, coin_to_sell, **kwargs):
        self.coin_to_buy = coin_to_buy.upper()
        self.amount = amount
        self.coin_to_sell = coin_to_sell
        super().__init__(**kwargs)
