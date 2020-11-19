import json
import unittest

from decimal_sdk import Wallet


class WalletTest(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet('door mystery clever video cave balance fence general harbor mean then cheap system hover '
                             'fitness hard lyrics sick energy length eyebrow crush bomb faculty')

    def test_wallet_keys_generation(self):
        public_key = self.wallet.get_public_key()
        self.assertEqual(
            'xpub6GSdLvwGrd5dVPyh4immypMdXmF8mDno4GhABBC4H1rGDGkWJoxSvn'
            'unTyTpCwegvPSU9KwnzFp9gjtQuEBA9KoKXQkBSPFHQDu4XW5gaso',
            public_key)

    def test_wallet_address_generation(self):
        address = self.wallet.get_address()
        self.assertEqual('dx1puvhlmaf9tvttrmwrsdc8jqxnvtva2hnfde0ex', address)

        with open('wallets.json') as test_wallets:
            wallets = json.load(test_wallets)['wallets']
            for wallet in wallets:
                test_wallet = Wallet(wallet['mnemonic'])
                test_address = test_wallet.get_address()
                self.assertEqual(wallet['address'], test_address)


if __name__ == '__main__':
    unittest.main()
