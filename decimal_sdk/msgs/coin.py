from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.tx_types import *
from decimal_sdk.types import Coin, Candidate, PublicKey


class SendCoinMsg(BaseMsg):
    type = COIN_SEND
    sender: str
    receiver: str
    coin: Coin

    def __init__(self, sender: str, receiver: str, coin: Coin):
        self.sender = sender
        self.receiver = receiver
        self.coin = coin

    def __dict__(self):
        return {'type': self.type,
                'value': {'sender': self.sender,
                          'receiver': self.receiver,
                          'coin': self.coin.__dict__()}
                }


class BuyCoinMsg(BaseMsg):
    type = COIN_BUY
    sender: str
    coin_to_buy: Coin
    max_coin_to_sell: Coin

    def __init__(self, sender: str, coin_to_buy: Coin, max_coin_to_sell: Coin):
        self.sender = sender
        self.coin_to_buy = coin_to_buy
        self.max_coin_to_sell = max_coin_to_sell

    def __dict__(self):
        return {'type': self.type,
                'value': {
                    'sender': self.sender,
                    'coin_to_buy': self.coin_to_buy.__dict__(),
                    'max_coin_to_sell': self.max_coin_to_sell.__dict__()}
                }


class SellCoinMsg(BaseMsg):
    type = COIN_SELL
    sender: str
    coin_to_sell: Coin
    min_coin_to_buy: Coin

    def __init__(self, sender: str, coin_to_sell: Coin, min_coin_to_buy: Coin):
        self.sender = sender
        self.coin_to_sell = coin_to_sell
        self.min_coin_to_buy = min_coin_to_buy

    def __dict__(self):
        return {'type': self.type,
                'value': {
                    'sender': self.sender,
                    'coin_to_sell': self.coin_to_sell.__dict__(),
                    'min_coin_to_buy': self.min_coin_to_buy.__dict__()}
                }


class SellAllCoinsMsg(BaseMsg):
    type = COIN_SELL_ALL
    sender: str
    coin_to_sell: Coin
    min_coin_to_buy: Coin

    def __init__(self, sender: str, coin_to_sell: Coin, min_coin_to_buy: Coin):
        self.sender = sender
        self.coin_to_sell = coin_to_sell
        self.min_coin_to_buy = min_coin_to_buy
        self.min_coin_to_buy.amount = '0'

    def __dict__(self):
        return {'type': self.type,
                'value': {
                    'sender': self.sender,
                    'coin_to_sell': self.coin_to_sell.__dict__(),
                    'min_coin_to_buy': self.min_coin_to_buy.__dict__()}
                }


class Delegate(BaseMsg):
    type = VALIDATOR_DELEGATE
    delegator_address: str
    validator_address: str
    coin: Coin

    def __init__(self, delegator_address: str, validator_address: str, coin: Coin):
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.coin = coin

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "delegator_address": self.delegator_address,
                    "validator_address": self.validator_address,
                    "coin": self.coin.__dict__()
                }}


class Unbound(BaseMsg):
    type = VALIDATOR_UNBOND
    delegator_address: str
    validator_address: str
    coin: Coin

    def __init__(self, delegator_address: str, validator_address: str, coin: Coin):
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.coin = coin

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "delegator_address": self.delegator_address,
                    "validator_address": self.validator_address,
                    "coin": self.coin.__dict__()
                }}


class DeclareCandidate(BaseMsg):
    type = VALIDATOR_CANDIDATE
    commission: int
    validator_addr: str
    reward_addr: str
    pub_key: PublicKey
    stake: Coin
    description: Candidate

    def __init__(self, commission: int, validator_addr: str, reward_addr: str, pub_key: PublicKey, stake: Coin,
                 description: Candidate):
        self.commission = commission
        self.validator_addr = validator_addr
        self.reward_addr = reward_addr
        self.pub_key = pub_key
        self.stake = stake
        self.description = description

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "commission": "",
                    "validator_addr": "",
                    "reward_addr": "",
                "pub_key": self.pub_key.__dict__(),
                "stake": self.stake.__dict__(),
                "description": self.description.__dict__()
                }}


class EditCandidate(BaseMsg):
    type = VALIDATOR_CANDIDATE_EDIT
    validator_address: str
    reward_address: str
    description: Candidate

    def __init__(self, validator_address: str, reward_address: str, description: Candidate):
        self.validator_address = validator_address
        self.reward_address = reward_address
        self.description = description

    def __dict__(self):
        return {"type": self.type,
                "value": { "validator_address": self.validator_address,
                           "reward_address": self.validator_address,
                           "description": self.description.__dict__()
                }}


class DisableEnableValidator(BaseMsg):
    type: str
    validator_address: str

    state = {
        "disable": VALIDATOR_SET_OFFLINE,
        "enable": VALIDATOR_SET_ONLINE
    }

    def __init__(self, set_state: str, validator_address: str):
        self.type = self.state[set_state]
        self.validator_address = validator_address

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "delegator_address": self.validator_address
                }}


class CreateCoinMsg(BaseMsg):
    type = COIN_CREATE
    sender: str
    title: str
    symbol: str
    crr: int
    initial_volume: str
    initial_reserve: str
    limit_volume: str

    def __init__(self, sender: str, title: str, symbol: str, crr: int, initial_volume: str, initial_reserve: str,
                 limit_volume: str):
        self.sender = sender
        self.title = title
        self.symbol = symbol
        self.crr = crr
        self.initial_volume = initial_volume
        self.initial_reserve = initial_reserve
        self.limit_volume = limit_volume

    def __dict__(self):
        return {'type': self.type, 'value': {'sender': self.sender, 'title': self.title, 'symbol': self.symbol,
                                             'constant_reserve_ratio': self.crr, 'initial_volume': self.initial_volume,
                                             'initial_reserve': self.initial_reserve,
                                             'limit_volume': self.limit_volume}}


class MultysigCreate(BaseMsg):
    type = MULTISIG_CREATE_WALLET
    sender: str
    owners: str
    weights: int
    threshold: int

    def __init__(self, sender: str, owners: str, weights: int, threshold: int):
        self.sender = sender
        self.owners = owners
        self.weights = weights
        self.threshold = threshold

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "sender": self.sender,
                    "owners": self.owners,
                    "weights": self.weights,
                    "threshold": self.threshold
                }}


class MultysigCreateTX(BaseMsg):
    type = MULTISIG_CREATE_TX
    sender: str
    wallet: str
    receiver: str
    coins: Coin

    def __init__(self, sender: str, wallet: str, receiver: str, coins: Coin):
        self.sender = sender
        self.wallet = wallet
        self.receiver = receiver
        self.coins = coins

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "sender": self.sender,
                    "wallet": self.wallet,
                    "receiver": self.receiver,
                    "coins": self.coins.__dict__()
                }}


class MultysigSignTX(BaseMsg):
    type = MULTISIG_SIGN_TX

    sender: str
    tx_id: str

    def __init__(self, sender: str, tx_id: str):
        self.sender: sender
        self.tx_id: tx_id

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "sender": self.sender,
                    "tx_id": self.tx_id
                }}


class MultisendSend:
    receiver: str
    coin: Coin

    def __init__(self, receiver: str, coin: Coin):
        self.receiver = receiver
        self.coin = coin

    def __dict__(self):
        return {'coin': self.coin, 'receiver': self.receiver}


class MultisendCoinMsg(BaseMsg):
    type = COIN_MULTISEND

    sender: str
    sends: [MultisendSend]

    def __init__(self, sender: str, sends: [MultisendSend]):
        self.sender = sender
        self.sends = sends

    def __dict__(self):
        return {'type': self.type,
                'value': {
                    'sender': self.sender,
                    'sends': [send.__dict__() for send in self.sends]
                }}


class SubmitProposal(BaseMsg):
    type = PROPOSAL_SUBMIT
    # todo check wallet can submit proposal
    content: str
    proposer: str
    voting_start_block: str
    voting_end_block: str

    def __init__(self, content: str, proposer: str, voting_start_block: str, voting_end_block: str):
        self.content = content
        self.proposer = proposer
        self.voting_start_block = voting_start_block
        self.voting_end_block = voting_end_block

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "content": self.content,
                    "proposer": self.proposer,
                    "voting_start_block": self.voting_start_block,
                    "voting_end_block": self.voting_end_block,
                }}


class VoteProposal(BaseMsg):
    type = PROPOSAL_VOTE
    proposal_id: int
    voter: str
    option: str

    def __init__(self, proposal_id: int, voter: str, option: str):
        self.proposal_id = proposal_id
        self.voter = voter
        self.option = option

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "proposal_id": self.proposal_id,
                    "voter": self.voter,
                    "option": self.option
                }}


class SwapHtlt(BaseMsg):
    type = SWAP_HTLT
    transfer_type: str
    sender: str
    recipient: str
    hashed_secret: str
    amount: Coin

    def __init__(self, transfer_type: str, sender: str, recipient: str, hashed_secret: str, amount: Coin):
        self.sender = sender
        self.recipient = recipient
        self.hashed_secret = hashed_secret
        self.amount = amount
        if transfer_type == "in":
            self.transfer_type = "2"
        else:
            self.transfer_type = "1"

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "transfer_type": self.transfer_type,
                    "from": self.sender,
                    "recipient": self.recipient,
                    "hashed_secret": self.hashed_secret,
                    "amount": self.amount.__dict__()
                }}


class SwapRedeem(BaseMsg):
    type = SWAP_REDEEM
    secret: str
    sender: str

    def __init__(self, secret: str, sender: str):
        self.secret = secret
        self.sender = sender

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "from": f'"{self.sender}", {self.secret}' #todo check how it works
                }}


class SwapRefund(BaseMsg):
    type = SWAP_REFUND
    sender: str
    hashed_secret: str

    def __init__(self, sender: str, hashed_secret: str):
        self.sender = sender
        self.hashed_secret = hashed_secret

    def __dict__(self):
        return {"type": self.type, "value": {
            "from": self.sender,
            "hashed_secret": self.hashed_secret
        }}




