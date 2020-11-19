from Cryptodome.Hash import SHA256, RIPEMD160
from mnemonic import Mnemonic
from bip32 import BIP32
import bech32

DERIVATION_PATH = "m/44'/60'/0'/0/0"


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
        self.__generate_address()

    def get_address(self) -> str:
        return self._address

    def get_private_key(self) -> str:
        pass

    def get_public_key(self) -> str:
        return self._public_key

    def __generate_address(self):
        sha256_object = SHA256.new(self._public_key_binary)
        sha256_hash = sha256_object.digest()
        ripemd160_object = RIPEMD160.new(sha256_hash)
        ripemd160_hash = ripemd160_object.digest()
        address = bech32.bech32_encode('dx', bech32.convertbits(ripemd160_hash, 8, 5))
        self._address = address
