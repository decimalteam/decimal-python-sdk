from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

receiver = "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g"
coin_name = "tdel"
coin_amount = 1

tx = SendCoinTransaction(wallet.get_address(), receiver, coin_name, coin_amount)
api.send_tx(tx, wallet, {"denom": "tdel"})

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import BuyCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

coin_to_buy = "del"
coin_to_sell = "dar"
coin_to_buy_amount = 0.1
coin_to_sell_limit = 0.5

tx2 = BuyCoinTransaction(wallet.get_address(), coin_to_buy, coin_to_sell, coin_to_buy_amount, coin_to_sell_limit)
api.send_tx(tx2, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import CreateCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

title = "My new coin w"
symbol = "MYBNWCNW"
crr = "45"
initial_reserve = "1000500000000000000000"
initial_volume = "5000000"
limit_volume = "10000000"
identity = 'e353b89e0de0a78974f9ecaf033721ac'

tx3 = CreateCoinTransaction(wallet.get_address(), title, symbol, crr, initial_volume,
                            initial_reserve, identity, limit_volume)
api.send_tx(tx3, wallet)
api.get

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import UpdateCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

title = "My new coin"
symbol = "MNC"
crr = "10"
initial_reserve = "1000000000000000000000"
initial_volume = "500000"
limit_volume = "1000000"
identity = 'e353b89e0de0a78974f9ecaf033721ac'

tx3 = UpdateCoinTransaction(wallet.get_address(), symbol, identity, limit_volume)
api.send_tx(tx3, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SellAllCoinsMsgTransaction

wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

coin_to_sell_name = "tdel"
coin_to_sell_amount = "1.1"
min_coin_to_buy_name = "finaltest"
min_coin_to_buy_amount = "1.1"

tx4 = SellAllCoinsMsgTransaction(wallet.get_address(), coin_to_sell_name, coin_to_sell_amount,
                                 min_coin_to_buy_name, min_coin_to_buy_amount)
api.send_tx(tx4, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DelegateTransaction

wallet = Wallet("exotic favorite initial tank bridge tuition broken hope sniff tiny fringe ice letter joke goddess skate raw similar link knife cable today table gain")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
coins_name = "tdel"
coin_amount = "1"

tx5 = DelegateTransaction(wallet.get_address(), validator_addr, coins_name, coin_amount)
api.send_tx(tx5, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import UnbondTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
coins_name = "tdel"
coin_amount = "10"
tx6 = UnbondTransaction(wallet.get_address(), validator_addr, coins_name, coin_amount)
api.send_tx(tx6, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DeclareCandidateTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

reward_addr = 'dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g'
# validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
validator_addr = wallet.get_validator_address()
coin_name = 'tdel'
coin_amount = "100000000000000000000"
pub_key = 'JRlv38BXuD1TvWQJ9ic1KHr8PzuOITZH3rD8Zm0Vj3Y='
commission = "0.100000000000000000"
moniker = 'my-node-123'
identity = ""
website = "hello.ru"
security_contact = "test@test.com"
details = "details node"

tx7 = DeclareCandidateTransaction(commission, validator_addr, reward_addr,
                 coin_name, coin_amount, moniker, identity, website, security_contact, details,
                 pub_key)
api.send_tx(tx7, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import EditCandidateTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

validator_address = wallet.get_validator_address()
reward_address = "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g"
moniker = 'my-node-123-edit'
identity = '321'
website = 'hello.ru'
security_contact = 'test@test.com'
details = 'details node'

tx8 = EditCandidateTransaction(validator_address, reward_address,
                 moniker, identity, website, security_contact, details)
api.send_tx(tx8, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DisableEnableValidatorTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

set_state = "disable" # "enable"
validator_address = wallet.get_validator_address()
tx9 = DisableEnableValidatorTransaction(set_state, validator_address)
api.send_tx(tx9, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultysigCreateTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

owners = ['dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g', 'dx1v9macmluxh7rk3zsd69v7dwv9fsjhctn2jfhz9']
weights = ['1', '1']
threshold = "2"
tx10 = MultysigCreateTransaction(wallet.get_address(), owners, weights, threshold)
api.send_tx(tx10, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultysigCreateTXTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

sender = 'dx1am6ke3l79kjzdqhwgx37em04mzg686ekf9p3pq'
receiver = 'dx13m9gxeru45wxlcqk9dxf4vlewslauwr8try0tl'
coin_name = 'tdel'
coin_amount = '10'

tx11 = MultysigCreateTXTransaction(sender, wallet.get_address(), receiver, coin_name, coin_amount)
api.send_tx(tx11, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultysigSignTXTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

tx_id = 'dxmstx1tqmjch2x5uk9wgnu8zl88rj6h4hy8rm8mtqfft'

tx12 = MultysigSignTXTransaction(wallet.get_address(), tx_id)
api.send_tx(tx12, wallet)

###########################################################################################

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
        "amount": '100'
    },
    {
        "receiver": 'dx13m9gxeru45wxlcqk9dxf4vlewslauwr8try0tl',
        "coin": 'tdel',
        "amount": '50'
    }
]

tx13 = MultisendCoinTransaction(wallet.get_address(), multisend)
api.send_tx(tx13, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI

api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
data = {
    "nonce": "34",
    "coin": "tdel",
    "amount": "100",
    "password": "123",
    "due_block": "999999999",
}

api.issue_check(wallet, data)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
data = {
    "check": 'ERp9FR24Vz19XGXddnESNVBhTKxh8Q38CyLC7JHm5wz2pJFZpzSavzRbUJNTFmvuopkiHCFQAWhZN9V4RvPYswuTsK1JHNjESrvLSWFUSvLXM35RrMacsREBKA42DqYBC4M1J6swMqpLP12g9WBYdJS4iuM3QEyi4HkjAqcZDZJ4ox8R36D7pJvT4UtovBHDfT5YEQRdafUDJYnUJyYeXtFphQnheWapAuXi92RnxeRbRneXoopGgq671Jsxa',
    "password": "123",
}
api.redeem_check(data, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftMintTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein1'
token_uri = 'uri'
id = '7777'
quantity = 2
reserve = 1
allow_mint = True

tx3 = NftMintTransaction(denom, id, wallet.get_address(), wallet.get_address(), quantity, reserve, token_uri, allow_mint)
api.send_tx(tx3, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftBurnTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein1'
id = '7777'
quantity = 1

tx3 = NftBurnTransaction(denom, id, wallet.get_address(), quantity)
api.send_tx(tx3, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftEditMetadataTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein1'
id = '7777'
token_uri = 'uri21'

tx3 = NftEditMetadataTransaction(denom, id, wallet.get_address(), token_uri)
api.send_tx(tx3, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftTransferTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein1'
id = '7777'
quantity = 1

tx3 = NftTransferTransaction(denom, id, wallet.get_address(), wallet.get_address(), quantity)
api.send_tx(tx3, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftDelegateTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein1'
id = '7777'
validator_address = 'dxvaloper1mvqrrrlcd0gdt256jxg7n68e4neppu5tk872z3'
quantity = 1

tx3 = NftDelegateTransaction(denom, id, wallet.get_address(), validator_address, quantity)
api.send_tx(tx3, wallet)

###########################################################################################

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftUnboundTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'Portwein1'
id = '7777'
validator_address = 'dxvaloper1mvqrrrlcd0gdt256jxg7n68e4neppu5tk872z3'
quantity = 1

tx3 = NftUnboundTransaction(denom, id, wallet.get_address(), validator_address, quantity)
api.send_tx(tx3, wallet)