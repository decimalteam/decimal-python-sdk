from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("exotic favorite initial tank bridge tuition broken hope sniff tiny fringe ice letter joke goddess skate raw similar link knife cable today table gain")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

receiver = "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g"
coin_name = "del"
coin_amount = 160.1
options = {
    "denom": coin_name,
    "memo": "sdk test"
}
tx = SendCoinTransaction(wallet.get_address(), receiver, coin_name, coin_amount)
api.estimate_tx_fee(tx, wallet, options)
api.send_tx(tx, wallet, options)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import BuyCoinTransaction
# wallet = Wallet("exotic favorite initial tank bridge tuition broken hope sniff tiny fringe ice letter joke goddess skate raw similar link knife cable today table gain")
# api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

coin_to_buy = "awsmcnn"
coin_to_sell = "del"
coin_to_buy_amount = 0.1
btt_price = api.get_coin_price('awsmcnn')
coin_to_sell_limit = coin_to_buy_amount*btt_price

fee_coin = "btt"
options = {
    # "denom": fee_coin,
    "memo": "message to send with transaction"
}

tx2 = BuyCoinTransaction(wallet.get_address(), coin_to_buy, coin_to_sell, coin_to_buy_amount, coin_to_sell_limit)
api.send_tx(tx2, wallet, options)

###########################################################################################

# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import CreateCoinTransaction
# wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
# api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
#
# title = "awesomeTestCoin"
# symbol = "AWSMCNN"
# crr = "10"
# initial_reserve = "1000000000000000000000"
# initial_volume = "500000000000000000000"
# limit_volume = "1000000000000000000000"
# identity = 'e353b89e0de0a78974f9ecaf033721ac'
#
# tx3 = CreateCoinTransaction(wallet.get_address(), title, symbol, crr, initial_volume,
#                             initial_reserve, identity, limit_volume)
# api.send_tx(tx3, wallet)
#
# ###########################################################################################


# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import UpdateCoinTransaction
# wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
# api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
#
# title = "My new awesomeTestCoin"
# symbol = "AWSMCNN"
# crr = "10"
# initial_reserve = "1000000000000000000000"
# initial_volume = "900000000000000000000"
# limit_volume = "1000000000000000000000"
# identity = 'e353b89e0de0a78974f9ecaf033721ac'
#
# tx3 = UpdateCoinTransaction(wallet.get_address(), symbol, identity, limit_volume)
# api.send_tx(tx3, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SellAllCoinsMsgTransaction

# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
wallet = Wallet("assume claim blind pony crane total glance hockey reform sentence brand tide decide solid party afford year oak fortune educate else remove vapor extend")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

coin_to_sell_name = "finaltest"
coin_to_sell_amount = 1000
min_coin_to_buy_name = "del"
min_coin_to_buy_amount = 1

tx4 = SellAllCoinsMsgTransaction(wallet.get_address(), coin_to_sell_name, coin_to_sell_amount,
                                 min_coin_to_buy_name, min_coin_to_buy_amount)
api.send_tx(tx4, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import DelegateTransaction
#
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
# coins_name = "finaltest"
# coin_amount = "1"
#
# tx5 = DelegateTransaction(wallet.get_address(), validator_addr, coins_name, coin_amount)
# api.send_tx(tx5, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import UnbondTransaction
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
# coins_name = "tdel"
# coin_amount = "10"
# tx6 = UnbondTransaction(wallet.get_address(), validator_addr, coins_name, coin_amount)
# api.send_tx(tx6, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DeclareCandidateTransaction
wallet = Wallet("bulk simple nephew below neutral robot swamp spoil hospital area choice narrow miss battle general mercy element test indoor salad captain fringe liar electric")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
reward_addr = wallet.get_address()
validator_addr = wallet.get_validator_address()
coin_name = 'tdel'
coin_amount = "10000000000000000000"
pub_key = 'KuFmdTdrHqDivlNxdjK7XpMml8PNkRvW3/oveYSN/xE='
commission = "0"
moniker = 'my-node-123'
identity = ""
website = "hello.ru"
security_contact = "test@test.com"
details = "details node"

tx7 = DeclareCandidateTransaction(commission, validator_addr, reward_addr,
                 coin_name, coin_amount, moniker, identity, website, security_contact, details,
                 pub_key)
api.send_tx(tx7, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import EditCandidateTransaction
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# validator_address = wallet.get_validator_address()
# reward_address = "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g"
# moniker = 'my-node-123-edit'
# identity = '321'
# website = 'hello.ru'
# security_contact = 'test@test.com'
# details = 'details node'
#
# tx8 = EditCandidateTransaction(validator_address, reward_address,
#                  moniker, identity, website, security_contact, details)
# api.send_tx(tx8, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import DisableEnableValidatorTransaction
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# set_state = "disable" # "enable"
# validator_address = wallet.get_validator_address()
# tx9 = DisableEnableValidatorTransaction(set_state, validator_address)
# api.send_tx(tx9, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import MultysigCreateTransaction
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# owners = ['dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g', 'dx1v9macmluxh7rk3zsd69v7dwv9fsjhctn2jfhz9']
# weights = ['1', '1']
# threshold = "2"
# tx10 = MultysigCreateTransaction(wallet.get_address(), owners, weights, threshold)
# api.send_tx(tx10, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import MultysigCreateTXTransaction
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# sender = 'dx1am6ke3l79kjzdqhwgx37em04mzg686ekf9p3pq'
# receiver = 'dx13m9gxeru45wxlcqk9dxf4vlewslauwr8try0tl'
# coin_name = 'tdel'
# coin_amount = '10'
#
# tx11 = MultysigCreateTXTransaction(sender, wallet.get_address(), receiver, coin_name, coin_amount)
# api.send_tx(tx11, wallet)
#
# ###########################################################################################
#
# from decimal_sdk import Wallet
# from decimal_sdk import DecimalAPI
# from decimal_sdk import MultysigSignTXTransaction
# wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
# api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
#
# tx_id = 'dxmstx1tqmjch2x5uk9wgnu8zl88rj6h4hy8rm8mtqfft'
#
# tx12 = MultysigSignTXTransaction(wallet.get_address(), tx_id)
# api.send_tx(tx12, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultisendCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

tx_id = 'dxmstx1tqmjch2x5uk9wgnu8zl88rj6h4hy8rm8mtqfft'
multisend = [
    {
        "receiver": 'dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g',
        "coin": 'tdel',
        "amount": 100.1
    },
    {
        "receiver": 'dx13m9gxeru45wxlcqk9dxf4vlewslauwr8try0tl',
        "coin": 'tdel',
        "amount": 100.2
    }
]

tx13 = MultisendCoinTransaction(wallet.get_address(), multisend)
api.send_tx(tx13, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI

api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
data = {
    "nonce": "100",
    "coin": "tdel",
    "amount": "102",
    "password": "123",
    "due_block": "999999999",
}

check = api.issue_check(wallet, data)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("ill expose excess top special proof force damage vicious crime carry people ill together shrug enact weekend uncle minimum ginger congress clinic wasp snake")
data = {
    "check": check,
    "password": "123",
}
api.redeem_check(data, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftMintTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
token_uri = 'uri22212'
id = '886688'
quantity = 212
reserve = 11
allow_mint = True

tx3 = NftMintTransaction(denom, id, wallet.get_address(), wallet.get_address(), quantity, reserve, token_uri, allow_mint)
api.send_tx(tx3, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftBurnTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["1", "3", "8"]

tx3 = NftBurnTransaction(denom, id, wallet.get_address(), sub_token_ids)
api.send_tx(tx3, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftEditMetadataTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein121'
id = '77772'
token_uri = 'uri2121'

tx3 = NftEditMetadataTransaction(denom, id, wallet.get_address(), token_uri)
api.send_tx(tx3, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftTransferTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["2", "4", "9", "200", "150"]

tx3 = NftTransferTransaction(denom, id, wallet.get_address(), "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g", sub_token_ids)
api.send_tx(tx3, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftDelegateTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["113", "111"]
validator_address = 'dxvaloper1mvqrrrlcd0gdt256jxg7n68e4neppu5tk872z3'

tx3 = NftDelegateTransaction(denom, id, wallet.get_address(), validator_address, sub_token_ids)
api.send_tx(tx3, wallet)
#
# ###########################################################################################
#
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftUnboundTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["113", "111"]
validator_address = 'dxvaloper1mvqrrrlcd0gdt256jxg7n68e4neppu5tk872z3'

tx3 = NftUnboundTransaction(denom, id, wallet.get_address(), validator_address, sub_token_ids)
api.send_tx(tx3, wallet)

############################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SwapRedeemTransaction
wallet = Wallet("exotic favorite initial tank bridge tuition broken hope sniff tiny fringe ice letter joke goddess skate raw similar link knife cable today table gain")

# wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

sender = wallet.get_address()
sent_from = '0x856F08B12cB844fa05CDF1eBfFd303B091D34d09'
amount = 2
recipient = 'dx1twj64nphm8zl98uxv7gnt6xg4tpkk4gyr3tux9'
token_name = 'muh coin'
token_symbol = 'coin'
from_chain = '2'
dest_chain = '1'
v = '0x1c',
r = '0xb8b3eb4980e649a65b7e136fbcafda4d12e3b11a40d8aaa7d951e13fbe483579'
s = '0x74de77f4a9f4045992cf6f220cff9be67a2c0332124e60af0a6791c9b0a64c36'

tx3 = SwapRedeemTransaction(sender, sent_from, recipient, amount, token_name, token_symbol, from_chain, dest_chain, v, r, s)
api.send_tx(tx3, wallet)

############################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SwapInitTransaction
wallet = Wallet("exotic favorite initial tank bridge tuition broken hope sniff tiny fringe ice letter joke goddess skate raw similar link knife cable today table gain")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

sender = wallet.get_address()
recipient = 'dx1twj64nphm8zl98uxv7gnt6xg4tpkk4gyr3tux9'
amount = 2
token_symbol = 'coin'
from_chain = '1'
dest_chain = '2'

tx7 = SwapInitTransaction(sender, recipient, amount, token_symbol, from_chain, dest_chain)
api.send_tx(tx7, wallet)