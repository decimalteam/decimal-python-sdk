import unittest

from decimal_sdk import Wallet
from decimal_sdk.transactions import SendCoinTransaction, BuyCoinTransaction, CreateCoinTransaction, \
    DelegateTransaction, UnbondTransaction, BurnCoinTransaction


class TransactionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.wallet = Wallet('ladder repeat ticket floor physical second social veteran torch kiss opera sheriff lunch tribe cause weasel stable oppose sugar visa visa warfare capital meat')

    def test_send_coin(self):
        tx = SendCoinTransaction(sender=self.wallet.get_address(),
                                 receiver='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g',
                                 denom='del',
                                 amount=1)
        # self.check_tx(tx, 'lg1p+YnF7Ly61x5aZXjGu2TBQ4uYemMVmpQxHyJ71VklO09jYhFeowLl8JUM59r1dQPjdeSYsfhV1dE1KIdqgw==')

    def test_buy_coin(self):
        tx1 = BuyCoinTransaction(sender=self.wallet.get_address(),
                                amount_to_buy=10,
                                coin_to_buy='FINALTEST',
                                coin_to_spend='del')
        # self.check_tx(tx1, '')

    def test_create_coin(self):
        tx2 = CreateCoinTransaction(sender=self.wallet.get_address(),
                                   title='Test coin',
                                   symbol='TESTTT',
                                   crr=45,
                                   initial_volume=50000,
                                   initial_reserve=100000,
                                   limit_volume=12000)
        # self.check_tx(tx2, '')

    def test_delegate(self):
        tx2 = DelegateTransaction(delegator_address=self.wallet.get_address(),
                                 validator_address='dxvaloper1azre0dtclv5y05ufynkhswzh0cwh4ktzr0huw2',
                                 amount=10,
                                 denom='del')
        self.check_tx(tx2, '')

    def test_unbond(self):
        tx3 = UnbondTransaction(delegator_address=self.wallet.get_address(),
                               validator_address='dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0',
                               amount=10,
                               denom='del')
        self.check_tx(tx3, '')

    def test_burn_coin(self):
        tx = BurnCoinTransaction(sender=self.wallet.get_address(),
                                 denom='del',
                                 amount=12)
        # self.check_tx(tx, '')

    # def check_tx(self, tx, signature):
    #     tx.sign(self.wallet)
    #     [print(i.signature) for i in tx.signatures]
    #     self.assertEqual(signature, tx.signatures[0].signature)


if __name__ == '__main__':
    unittest.main()
