from mnemonic import Mnemonic
from bip32 import BIP32
import bech32

DERIVATION_PATH = "m/44'/60'/0'/0"


class Wallet:

    def __init__(self, mnemonic: str = None):
        mnemo = Mnemonic('english')
        if not mnemonic:
            mnemonic = mnemo.generate()
        self.mnemonic = mnemonic
        # Generate and save seed
        seed = mnemo.to_seed(mnemonic)
        self._seed = seed
        # Derive public key
        bip32 = BIP32.from_seed(seed)
        self._public_key = bip32.get_xpub_from_path(DERIVATION_PATH)
        self._public_key_binary = bip32.get_pubkey_from_path(DERIVATION_PATH)

    def get_address(self) -> str:
        return bech32.encode('dx', 0, self._public_key_binary[2:])

    def get_private_key(self) -> str:
        pass

    def get_public_key(self) -> str:
        return self._public_key
