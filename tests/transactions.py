import unittest

from decimal_sdk import Wallet
from decimal_sdk.transactions import Transaction, SendCoinTransaction
from decimal_sdk.types import SendCoinTx, Coin, create_std_sign_tx, SignMeta


class TransactionsTest(unittest.TestCase):
    def test_tx_signature(self):
        wallet = Wallet('hollow luggage slice soup leg vague icon walnut session candy improve struggle')
        private_key = wallet.get_private_key()

        tx = SendCoinTx(sender='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g', to='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g',
                        coin=Coin(denom='del', amount='1000000000000000000'), memo='sdk test')
        # tx = SendCoinTransaction(to='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g', coin='del', value=1)
        tx = create_std_sign_tx(tx, SignMeta('18', 'decimal-devnet-11-20-18-00', '7'))
        tx.sign(private_key)
        self.assertEqual('lg1p+YnF7Ly61x5aZXjGu2TBQ4uYemMVmpQxHyJ71VklO09jYhFeowLl8JUM59r1dQPjdeSYsfhV1dE1KIdqgw==',
                         tx.signatures[0])


if __name__ == '__main__':
    unittest.main()
