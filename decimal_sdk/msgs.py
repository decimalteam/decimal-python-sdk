import rlp
from rlp.sedes import text


class Coin(rlp.Serializable):
    denom: str
    amount: str

    fields = [
        ('denom', text),
        ('amount', text)
    ]

    def __dict__(self):
        return {'denom': self.denom, 'amount': self.amount}


class BaseMsgValue(rlp.Serializable):

    def __init__(self, *args, **kwargs):
        if kwargs.get('_meta', None) is not None:
            self._meta = kwargs.get('_meta')
            kwargs.pop('_meta')
            super().__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)


class SendCoinMsgValue(rlp.Serializable):
    coin: Coin
    receiver: str
    sender: str

    fields = [
        ('coin', Coin),
        ('receiver', text),
        ('sender', text)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __dict__(self):
        return {'coin': self.coin.__dict__(), 'receiver': self.receiver, 'sender': self.sender}