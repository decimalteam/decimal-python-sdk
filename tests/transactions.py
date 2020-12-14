import unittest

from decimal_sdk import Wallet
from decimal_sdk.msgs.coin import SendCoinMsg
from decimal_sdk.transactions import SendCoinTransaction
from decimal_sdk.types import Coin, SignMeta, StdSignMsg


class TransactionsTest(unittest.TestCase):
    def test_tx_signature(self):
        wallet = Wallet('hollow luggage slice soup leg vague icon walnut session candy improve struggle')
        tx = SendCoinTransaction(sender=wallet.get_address(),
                                 receiver='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g',
                                 denom='del',
                                 amount=1)
        tx.sign(wallet)
        self.assertEqual('lg1p+YnF7Ly61x5aZXjGu2TBQ4uYemMVmpQxHyJ71VklO09jYhFeowLl8JUM59r1dQPjdeSYsfhV1dE1KIdqgw==',
                         tx.signatures[0].signature)


if __name__ == '__main__':
    unittest.main()
