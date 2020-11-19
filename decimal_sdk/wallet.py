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

        if not mnemo.check(mnemonic):
            raise Exception('Invalid Mnemonic')
        self.__mnemonic = mnemonic

        # Generate and save seed
        seed = mnemo.to_seed(mnemonic)
        self._seed = seed
        # Derive public key
        self.__generate_keys()
        self.__generate_address()

    def get_address(self) -> str:
        return self._address

    def get_private_key(self) -> str:
        pass

    def get_public_key(self) -> str:
        return self._public_key

    def __generate_address(self):
        prepared_hash = self.__hash_public_key()
        address = bech32.bech32_encode('dx', bech32.convertbits(prepared_hash, 8, 5))
        self._address = address

    def __generate_keys(self):
        bip32 = BIP32.from_seed(self._seed)
        self._public_key = bip32.get_xpub_from_path(DERIVATION_PATH)
        self._public_key_binary = bip32.get_pubkey_from_path(DERIVATION_PATH)

    def __hash_public_key(self):
        sha256_hash = SHA256.new(self._public_key_binary).digest()
        ripemd160_hash = RIPEMD160.new(sha256_hash).digest()
        return ripemd160_hash
