from decimal_sdk import Wallet
from decimal_sdk.msgs.coin import SendCoinMsg
from decimal_sdk.types import Coin


class SendCoinTx:
    message: SendCoinMsg

    def __init__(self, to: str, ticker: str, value: float, wallet: Wallet, **kwargs):
        receiver = wallet.get_address()
        if kwargs['receiver']:
            receiver = kwargs['receiver']
        coin = Coin(ticker, str(value))
        self.message = SendCoinMsg(to, receiver, coin)
