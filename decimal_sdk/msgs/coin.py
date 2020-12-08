from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.tx_types import COIN_SEND, COIN_BUY
from decimal_sdk.types import Coin


class SendCoinMsg(BaseMsg):
    type = COIN_SEND
    sender: str
    receiver: str
    coin: Coin

    def __init__(self, sender: str, receiver: str, coin: Coin):
        self.sender = sender
        self.receiver = receiver
        self.coin = coin

    def __dict__(self):
        return {'type': self.type,
                'value': {'sender': self.sender, 'receiver': self.receiver, 'coin': self.coin.__dict__()}}


class BuyCoinMsg(BaseMsg):
    type = COIN_BUY
    sender: str
    coin_to_buy: Coin
    max_coin_to_sell: Coin

    def __init__(self, sender: str, coin_to_buy: Coin, max_coin_to_sell: Coin):
        self.sender = sender
        self.coin_to_buy = coin_to_buy
        self.max_coin_to_sell = max_coin_to_sell

    def __dict__(self):
        return {'type': self.type, 'sender': self.sender, 'coin_to_buy': self.coin_to_buy.__dict__(),
                'max_coin_to_sell': self.max_coin_to_sell.__dict__()}
