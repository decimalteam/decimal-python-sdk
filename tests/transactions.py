import unittest

from decimal_sdk import Wallet
from decimal_sdk.msgs.coin import SendCoinMsg
from decimal_sdk.types import Coin, SignMeta, Tx, StdSignMsg


class TransactionsTest(unittest.TestCase):
    def test_tx_signature(self):
        wallet = Wallet('hollow luggage slice soup leg vague icon walnut session candy improve struggle')

        tx = Tx(memo='sdk test')
        meta = SignMeta('18', 'decimal-devnet-11-20-18-00', '7')
        std_msg = StdSignMsg(tx, meta)
        std_msg.add_msg(
            SendCoinMsg(sender=wallet.get_address(),
                        receiver='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g',
                        coin=Coin(denom='del', amount='1000000000000000000')
                        )
        )
        # tx = SendCoinTx(wallet=etc, )
        std_msg.sign(wallet)
        self.assertEqual('lg1p+YnF7Ly61x5aZXjGu2TBQ4uYemMVmpQxHyJ71VklO09jYhFeowLl8JUM59r1dQPjdeSYsfhV1dE1KIdqgw==',
                         std_msg.signatures[0].signature)


if __name__ == '__main__':
    unittest.main()
