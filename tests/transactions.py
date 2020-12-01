import unittest

from decimal_sdk import Wallet
from decimal_sdk.transactions import Transaction, SendCoinTransaction


class TransactionsTest(unittest.TestCase):
    def test_tx_signature(self):
        wallet = Wallet('hollow luggage slice soup leg vague icon walnut session candy improve struggle')
        private_key = wallet.get_private_key()
        tx = SendCoinTransaction(to='dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g', coin='del', value=1)
        tx.sign(private_key)
        self.assertEqual('KlvVn/tUBBYMQVfSOA99ZT4qkxKfXEAloyGztcCi8DdZLvjunc+kcpiSEDbbjiaayxUf3etBnWgcMuv6IJoENg==',
                         tx.signature)


if __name__ == '__main__':
    unittest.main()
