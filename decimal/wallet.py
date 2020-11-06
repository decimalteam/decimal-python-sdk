from mnemonic import Mnemonic


class Wallet:
    def __init__(self, mnemonic: str = None):
        if not mnemonic:
            mnemonic = Mnemonic('english').generate()
        self.mnemonic = mnemonic

    def get_address(self) -> str:
        pass

    def get_private_key(self) -> str:
        pass

    def get_public_key(self) -> str:
        pass
