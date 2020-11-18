import unittest

from decimal_sdk  import Wallet


class WalletTest(unittest.TestCase):
    def test_wallet_address_generation(self):
        wallet = Wallet('door mystery clever video cave balance fence general harbor mean then cheap system hover '
                        'fitness hard lyrics sick energy length eyebrow crush bomb faculty ')
        address = wallet.get_address()
        self.assertEqual('dx1puvhlmaf9tvttrmwrsdc8jqxnvtva2hnfde0ex', address)


if __name__ == '__main__':
    unittest.main()
