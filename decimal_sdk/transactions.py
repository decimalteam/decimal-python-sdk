from decimal_sdk import Wallet
from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.msgs.coin import SendCoinMsg, BuyCoinMsg, CreateCoinMsg
from decimal_sdk.types import Signature, StdSignMsg, SignMeta, Fee, Coin
from decimal_sdk.utils import prepare_number


class Transaction:
    fee: Fee
    memo: str
    meta: SignMeta
    signatures = []
    msgs = []
    signer: StdSignMsg
    message: BaseMsg

    def __init__(self, **kwargs):
        self.meta = SignMeta()
        self.fee = Fee([], '0')
        self.memo = 'sdk test'
        self.signer = StdSignMsg(self, meta=self.meta)
        self.signer.add_msg(self.message)

    def add_msg(self, msg: BaseMsg):
        self.msgs.append(msg)

    def sign(self, wallet: Wallet):
        self.signer.sign(wallet)
        self.signatures = self.signer.signatures


class SendCoinTransaction(Transaction):
    message: SendCoinMsg

    def __init__(self, sender, receiver, denom, amount, **kwargs):
        coin = Coin(denom, prepare_number(amount))
        self.message = SendCoinMsg(sender, receiver, coin)
        super().__init__(**kwargs)


class BuyCoinTransaction(Transaction):
    message: BuyCoinMsg

    def __init__(self, sender, coin_to_buy, coin_to_spend, amount_to_buy, limit=100000000000, **kwargs):
        coin_to_buy = Coin(coin_to_buy, prepare_number(amount_to_buy))
        max_coin_to_sell = Coin(coin_to_spend, prepare_number(limit))
        self.message = BuyCoinMsg(sender, coin_to_buy, max_coin_to_sell)
        super().__init__(**kwargs)


class CreateCoinTransaction(Transaction):
    message: CreateCoinMsg

    def __init__(self, sender, title, symbol, crr, initial_volume, initial_reserve, limit_volume, **kwargs):
        self.message = CreateCoinMsg(sender, title, symbol, crr, initial_volume, initial_reserve, limit_volume)
        super().__init__(**kwargs)


class DelegateTransaction(Transaction):
    pass


class UnbondTransaction(Transaction):
    pass
