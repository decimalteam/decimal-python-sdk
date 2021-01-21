import hashlib

class Check:
    chain_id: str
    coin: str
    amount: int
    nonce: bytearray
    due_block: int
    lock: int
    v: int
    r: int
    s: int

    def get_sender(self):
        return self.recover_plain(self.hash(), self.r, self.s, self.v)

    def lock_pub_key_(self):
        pass

    def hash_without_lock(self):
        pass

    def hash(self):
        pass

    def hash_full(self):
        pass

    def sign(self):
        pass

    def set_signature(self, sig: bytearray):
        self.r = sig[0:32]
        self.s = sig[32:64]
        self.v = sig[64] + 27

    def parse_check(self):
        pass

    # def rpl_hash(self, x):
    #     hw = hashlib.
    #     hashlib.sha3_256

    def recover_plain(self, sighash, r, s, v):
        pass