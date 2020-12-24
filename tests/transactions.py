import unittest

from decimal_sdk import Wallet
from decimal_sdk.msgs.coin import SendCoinMsg
from decimal_sdk.transactions import SendCoinTransaction, BuyCoinTransaction, CreateCoinTransaction, \
    DelegateTransaction, UnbondTransaction
from decimal_sdk.types import Coin, SignMeta, StdSignMsg


class TransactionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.wallet = Wallet('hollow luggage slice soup leg vague icon walnut session candy improve struggle')

    def test_send_coin(self):
        tx = SendCoinTransaction(sender=self.wallet.get_address(),
                                 receiver='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g',
                                 denom='del',
                                 amount=1)
        self.check_tx(tx, 'lg1p+YnF7Ly61x5aZXjGu2TBQ4uYemMVmpQxHyJ71VklO09jYhFeowLl8JUM59r1dQPjdeSYsfhV1dE1KIdqgw==')

    def test_buy_coin(self):
        tx = BuyCoinTransaction(sender=self.wallet.get_address(),
                                amount=10,
                                denom='del')
        self.check_tx(tx, '')

    def test_create_coin(self):
        tx = CreateCoinTransaction(sender=self.wallet.get_address(),
                                   title='Test coin',
                                   symbol='TESTTT',
                                   crr=45,
                                   initial_volume=50000,
                                   initial_reserve=100000,
                                   limit_volume=12000)

    def test_delegate(self):
        tx = DelegateTransaction(delegator_address=self.wallet.get_address(),
                                 validator_address='dxvaloper1azre0dtclv5y05ufynkhswzh0cwh4ktzr0huw2',
                                 amount=10,
                                 denom='del')
        self.check_tx(tx, '')

    def test_unbond(self):
        tx = UnbondTransaction(delegator_address=self.wallet.get_address(),
                               validator_address='dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0',
                               amount=10,
                               denom='del')
        self.check_tx(tx, '')

    def check_tx(self, tx, signature):
        tx.sign(self.wallet)
        self.assertEqual(signature, tx.signatures[0].signature)


if __name__ == '__main__':
    unittest.main()
