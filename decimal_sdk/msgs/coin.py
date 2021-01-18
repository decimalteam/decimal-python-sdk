from decimal_sdk.msgs.base import BaseMsg
from decimal_sdk.tx_types import *
from decimal_sdk.types import Coin


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


    def __init__(self):
        pass

    def __dict__(self):
        return {"type": self.type,
                "value": {
                    "commission": "",
                    "validator_addr": "",
                    "reward_addr": "",
                # "pub_key": {
                #     type: 'tendermint/PubKeyEd25519',
                #     value: data.pubKey,
                # },
                # "stake": {
                #     denom: data.coin.toLowerCase(),
                #     amount: getAmountToUNI(data.stake),
                # },
                # "description": {
                #     moniker: data.description.moniker,
                #     identity: data.description.identity,
                #     website: data.description.website,
                #     security_contact: data.description.securityContact,
                #     details: data.description.details,
                # },
                }}


class EditCandidate(BaseMsg):
    type = VALIDATOR_CANDIDATE_EDIT
    validator_address: str
    reward_address: str
    description: str

    def __init__(self):
        pass

    def __dict__(self):
        return {"type": self.type, }


class DisableEnableValidator(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


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
    def __dict__(self):
        return {"type": self.type, }


class MultysigCreateTX(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


class MultysigSignTX(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


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
        return {'type': self.type, 'value': {'sender': self.sender, 'sends': [send.__dict__() for send in self.sends]}}


class SubmitProposal(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


class VoteProposal(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


class SwapHtlt(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


class SwapRedeem(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


class SwapRefund(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }


class GetValue(BaseMsg):
    def __dict__(self):
        return {"type": self.type, }



