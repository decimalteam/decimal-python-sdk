from .wallet import Wallet
from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.types import Signature, StdSignMsg, SignMeta, Fee, Coin, Candidate
from decimal_sdk.utils import prepare_number
from decimal_sdk.msgs.msgs import (SendCoinMsg, BuyCoinMsg, CreateCoinMsg, SellAllCoinsMsg,
                                   DelegateMsg, UnboundMsg,
                                   DeclareCandidateMsg, EditCandidateMsg,
                                   DisableEnableValidatorMsg,
                                   MultysigCreateMsg, MultysigCreateTXMsg, MultysigSignTXMsg, MultisendSend, MultisendCoinMsg,
                                   SubmitProposalMsg, VoteProposalMsg,
                                   SwapHtltMsg, SwapRedeemMsg, SwapRefundMsg)


class Transaction:
    fee: Fee
    memo: str
    meta: SignMeta
    signatures = []
    msgs = []
    signer: StdSignMsg
    message: BaseMsg

    def __init__(self, **kwargs):
        self.meta = SignMeta()
        self.fee = Fee([], '0')
        self.memo = 'sdk test'
        self.signer = StdSignMsg(self, meta=self.meta)
        self.signer.add_msg(self.message)

    def add_msg(self, msg: BaseMsg):
        self.msgs.append(msg)

    def sign(self, wallet: Wallet):
        self.signer.sign(wallet)
        self.signatures = self.signer.signatures


class SendCoinTransaction(Transaction):
    message: SendCoinMsg

    def __init__(self, sender, receiver, denom, amount, **kwargs):
        coin = Coin(denom, prepare_number(amount))
        self.message = SendCoinMsg(sender, receiver, coin)
        super().__init__(**kwargs)


class BuyCoinTransaction(Transaction):
    message: BuyCoinMsg

    def __init__(self, sender, coin_to_buy, coin_to_spend, amount_to_buy, limit=100000000000, **kwargs):
        coin_to_buy = Coin(coin_to_buy, prepare_number(amount_to_buy))
        max_coin_to_sell = Coin(coin_to_spend, prepare_number(limit))
        self.message = BuyCoinMsg(sender, coin_to_buy, max_coin_to_sell)
        super().__init__(**kwargs)


class CreateCoinTransaction(Transaction):
    message: CreateCoinMsg

    def __init__(self, sender, title, symbol, crr, initial_volume, initial_reserve, limit_volume, **kwargs):
        self.message = CreateCoinMsg(sender, title, symbol, crr, initial_volume, initial_reserve, limit_volume)
        super().__init__(**kwargs)


class SellAllCoinsMsgTransaction(Transaction):
    message: SellAllCoinsMsg

    def __init__(self, sender: str, coin_to_sell_denom: str, coin_to_sell_amount: str, min_coin_to_buy_denom: str,
                 min_coin_to_buy_amount: str, **kwargs):
        coin_to_sell = Coin(coin_to_sell_denom, coin_to_sell_amount)
        min_coin_to_buy = Coin(min_coin_to_buy_denom, min_coin_to_buy_amount)
        self.message = SellAllCoinsMsg(sender, coin_to_sell, min_coin_to_buy)
        super().__init__(**kwargs)


class DelegateTransaction(Transaction):
    message: DelegateMsg

    def __init__(self, delegator_address: str, validator_address: str, denom: str, amount: str, **kwargs):
        coin = Coin(denom, amount)
        self.message = DelegateMsg(delegator_address, validator_address, coin)
        super().__init__(**kwargs)


class UnbondTransaction(Transaction):
    message: UnboundMsg

    def __init__(self, delegator_address: str, validator_address: str, denom: str, amount: str, **kwargs):
        coin = Coin(denom, amount)
        self.message = UnboundMsg(delegator_address, validator_address, coin)
        super().__init__(**kwargs)


class DeclareCandidateTransaction(Transaction):
    message: DeclareCandidateMsg

    def __init__(self, commission: int, validator_addr: str, reward_addr: str,
                 denom: str, amount: str,
                 moniker: str, identity: str, website: str, security_contact: str, details: str,
                 key_value: str, key_type: str = 'tendermint/PubKeyEd25519', **kwargs):
        stake = Coin(denom, amount)
        pub_key = Signature(key_value, key_type)
        description = Candidate(moniker, identity, website, security_contact, details)
        self.message = DeclareCandidateMsg(commission, validator_addr, reward_addr, pub_key, stake, description)
        super().__init__(**kwargs)


class EditCandidateTransaction(Transaction):
    message: EditCandidateMsg

    def __init__(self, validator_address: str, reward_address: str,
                 moniker: str, identity: str, website: str, security_contact: str, details: str, **kwargs):
        description = Candidate(moniker, identity, website, security_contact, details)
        self.message = EditCandidateMsg(validator_address, reward_address, description)
        super().__init__(**kwargs)


class DisableEnableValidatorTransaction(Transaction):
    message: DisableEnableValidatorMsg

    def __init__(self, set_state: str, validator_address: str, **kwargs):
        self.message = DisableEnableValidatorMsg(set_state, validator_address)
        super().__init__(**kwargs)


class MultysigCreateTransaction(Transaction):
    message: MultysigCreateMsg

    def __init__(self, sender: str, owners: str, weights: int, threshold: int, **kwargs):
        self.message = MultysigCreateMsg(sender, owners, weights, threshold)
        super().__init__(**kwargs)


class MultysigCreateTXTransaction(Transaction):
    message: MultysigCreateTXMsg

    def __init__(self, sender: str, wallet: str, receiver: str, denom: str, amount: str, **kwargs):
        coin = Coin(denom, amount)
        self.message = MultysigCreateTXMsg(sender, wallet, receiver, coin)
        super().__init__(**kwargs)


class MultysigSignTXTransaction(Transaction):
    message: MultysigSignTXMsg

    def __init__(self, sender: str, tx_id: str, **kwargs):
        self.message = MultysigSignTXMsg(sender, tx_id)
        super().__init__(**kwargs)


class MultisendCoinTransaction(Transaction):
    message: MultisendCoinMsg
    # todo

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SubmitProposalTransaction(Transaction):
    message: SubmitProposalMsg

    def __init__(self, content: str, proposer: str, voting_start_block: str, voting_end_block: str, **kwargs):
        self.message = SubmitProposalMsg(content, proposer, voting_start_block, voting_end_block)
        super().__init__(**kwargs)


class VoteProposalTransaction(Transaction):
    message: VoteProposalMsg

    def __init__(self, proposal_id: int, voter: str, option: str, **kwargs):
        self.message = VoteProposalMsg(proposal_id, voter, option)
        super().__init__(**kwargs)


class SwapHtltTransaction(Transaction):
    message: SwapHtltMsg

    def __init__(self, transfer_type: str, sender: str, recipient: str, hashed_secret: str, denom: str, amount: str, **kwargs):
        coin = Coin(denom, prepare_number(amount))
        self.message = SwapHtltMsg(transfer_type, sender, recipient, hashed_secret, coin)
        super().__init__(**kwargs)


class SwapRedeemTransaction(Transaction):
    message: SwapRedeemMsg

    def __init__(self, secret: str, sender: str, **kwargs):
        self.message = SwapRedeemMsg(secret, sender)
        super().__init__(**kwargs)


class SwapRefundTransaction(Transaction):
    message: SwapRefundMsg

    def __init__(self, sender: str, hashed_secret: str, **kwargs):
        self.message = SwapRefundMsg(sender, hashed_secret)
        super().__init__(**kwargs)
