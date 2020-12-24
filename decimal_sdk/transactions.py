from decimal_sdk import Wallet
from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.msgs.coin import SendCoinMsg
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
    pass


class CreateCoinTransaction(Transaction):
    pass


class DelegateTransaction(Transaction):
    pass


class UnbondTransaction(Transaction):
    pass
