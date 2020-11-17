from mnemonic import Mnemonic
from bip32 import BIP32
import bech32


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
        self._bip32 = bip32
        self._public_key = bip32.get_xpub_from_path([0])

    def get_address(self) -> str:
        pass

    def get_private_key(self) -> str:
        pass

    def get_public_key(self) -> str:
        return self._public_key
