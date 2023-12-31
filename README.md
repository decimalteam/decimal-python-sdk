# Decimal Python SDK

Check out these links:
- [Decimal SDK docs](https://help.decimalchain.com/api-sdk/).
- [Decimal Console site](https://console.decimalchain.com/).

## Wallet API
### Generate new wallet
```python
from decimal_sdk import Wallet

wallet = Wallet()
```
### Generate wallet from mnemonic*
*if no mnemonic provided Wallet() will create instance with autogenerated mnemonic

```python
from decimal_sdk import Wallet

wallet = Wallet('erase august mask elevator sand picture north there apple equal anchor target')
```
### Get wallet address
```python
from decimal_sdk import Wallet

wallet = Wallet()
wallet.get_address() # returns wallet address
wallet.get_mnemonic() # returns wallet mnemonic
```

## Get DecimalAPI to perform transactions
To initiate api you have to pass address of the gateway for network you will work with 
```python
from decimal_sdk import DecimalAPI
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
```

## API usage
After you initialized api instance, you can use its` send_tx() method to send prepared transaction.
Transaction creation examples can be found in this file.
```python
from decimal_sdk import DecimalAPI
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
api.send_tx(prepared_transaction, wallet)
```

## Options
To alter memo send with transaction or to use custom coin to pay fee with you can pass to send_tx() third argument: dictionary "options"
- "memo" is used to send message with transaction
- "denom" is used to alter coin which will be used to pay fee for the transaction

```python
from decimal_sdk import DecimalAPI
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
fee_coin = "del"
memo = "message to send with transaction"
options = {
    "denom":fee_coin,
    "memo": memo,
}
api.send_tx(prepared_transaction, wallet, options)
```

### DecimalAPI methods
methods called like
```python
from decimal_sdk import DecimalAPI
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
wallet = Wallet('erase august mask elevator sand picture north there apple equal anchor target')
api.method_name(args) 
```

* send_tx(transaction, wallet, options) - send prepared transaction 
* get_tx_by_hash(hash) - check transaction by Hash
* estimate_tx_fee(transaction, wallet, options) - used the same way as api.send_tx(), returns transaction fee
* get_coin("coin_ticker") - get info about specified coin 
* get_coin_price("coin_ticker") - get price of specified coin 
* get_coins_list(limit, offset) - get list of available coins, default limit of coins to show is 10 
* get_my_transactions(wallet.get_address(), limit, offset) - get list of transactions 
* get_address(wallet.get_address()) - get data about address state including info about owned NFT 
* get_nonce(wallet.get_address()) - get data about nonce for address 
* get_stakes(wallet.get_address()) - get data about stakes for address 
* get_validator("validator_address") - get data about validator 
* get_tx("tx_hash") - get data about transaction by hash 
* get_nft("nft_id", wallet) - get json with subtokens of token (owner, reserve, subId, delegated, validator) passed wallet should be the wallet of the owner 
* get_nft_stakes(wallet.get_address()) - get data about nft stakes for address
* get_multisig()
* get_multisigs()
* get_txs_multisign()

## Send Coin Transaction
```python
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

receiver = "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g"
coin_name = "tdel"
coin_amount = 1
fee_coin = "tdel"
options = {
    "denom":fee_coin,
    "memo": "message to send with transaction"
}
tx = SendCoinTransaction(wallet.get_address(), receiver, coin_name, coin_amount)
api.send_tx(tx, wallet, options)
```

## Send All Coin Transaction

```python
from decimal_sdk.methods import SendAllCoin
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI


api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("YOUR MNEMO")
receiver = 'dx1wvh0h4nfkvzkxzun35wh6pyrl88xn5rhsrgns9'
coin_name = 'tdel'
options = {
    "memo": "SEND ALL MY MONEY"
}

SendAllCoin(api, wallet, receiver, coin_name, options)

```


## Buy Coin Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import BuyCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

coin_to_buy = "del"
coin_to_sell = "dar"
coin_to_buy_amount = 0.1
coin_to_sell_limit = 0.5 # limitation of money which will be spent to buy coin

fee_coin = "del"
options = {
    "denom":fee_coin,
    "memo": "message to send with transaction"
}

tx2 = BuyCoinTransaction(wallet.get_address(), coin_to_buy, coin_to_sell, coin_to_buy_amount, coin_to_sell_limit)
api.send_tx(tx2, wallet, options)

```

## Create Coin Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import CreateCoinTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

title = "My new coin MN"
symbol = "MNCMNCMN"
crr = "10"
initial_reserve = "1000000000000000000000"
initial_volume = "500000"
limit_volume = "1000000"
identity = 'e353b89e0de0a78974f9ecaf033721ac'

tx3 = CreateCoinTransaction(wallet.get_address(), title, symbol, crr, initial_volume,
                            initial_reserve, identity, limit_volume)
api.send_tx(tx3, wallet)

```

## Update Coin Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import UpdateCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

symbol = "MNC"
identity = 'e353b89e0de0a78974f9ecaf033721ac'
limit_volume = "1000000"

tx3 = UpdateCoinTransaction(wallet.get_address(), symbol, identity, limit_volume)
api.send_tx(tx3, wallet)

```

## Burn Coin Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import BurnCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

tx = BurnCoinTransaction(sender=wallet.get_address(),
                                 denom='del',
                                 amount=1)
api.send_tx(tx, wallet)

```

## Sell All Coins Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SellAllCoinsMsgTransaction

wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

coin_to_sell_name = "btt"
coin_to_sell_amount = 0 # must be zero 
min_coin_to_buy_name = "del"
min_coin_to_buy_amount = 0 # must be zero 

tx4 = SellAllCoinsMsgTransaction(wallet.get_address(), coin_to_sell_name, coin_to_sell_amount,
                                 min_coin_to_buy_name, min_coin_to_buy_amount)
api.send_tx(tx4, wallet)

```

## Delegate Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DelegateTransaction

wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
coins_name = "finaltest"
coin_amount = 1

tx5 = DelegateTransaction(wallet.get_address(), validator_addr, coins_name, coin_amount)
api.send_tx(tx5, wallet)

```

## Unbond Transaction
```python

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

```

## Declare Candidate Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DeclareCandidateTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

reward_addr = 'dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g'
# validator_addr = "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0"
validator_addr = wallet.get_validator_address()
coin_name = 'tdel'
coin_amount = 10
pub_key = 'JRlv38BXuD1TvWQJ9ic1KHr8PzuOITZH3rD8Zm0Vj3Y='
commission = "0.1" # 1 is 100%, here commission set to 10% 
moniker = 'my-node-123'
identity = "123"
website = "hello.ru"
security_contact = "test@test.com"
details = "details node"

tx7 = DeclareCandidateTransaction(commission, validator_addr, reward_addr,
                 coin_name, coin_amount, moniker, identity, website, security_contact, details,
                 pub_key)
api.send_tx(tx7, wallet)

```

## Edit Candidate Transaction
```python

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

```
## Disable/Enable Validator Transaction 
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DisableEnableValidatorTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

set_state = "disable" # "enable"
validator_address = wallet.get_validator_address()
tx9 = DisableEnableValidatorTransaction(set_state, validator_address)
api.send_tx(tx9, wallet)

```
## Multisig Create Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultysigCreateTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

owners = ['dxaasd13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g', 'dx1v9macmluxh7rk3zsd69v7dwv9fsjhctn2jfhz9']
weights = ['1', '1']
threshold = "2"
tx10 = MultysigCreateTransaction(wallet.get_address(), owners, weights, threshold)
api.send_tx(tx10, wallet)

```

## Multisig Create TX Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultysigCreateTXTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

sender = 'dx1am6ke3l79kjzdqhwgx37em04mzg686ekf9p3pq'
receiver = 'dx13m9gxeru45wxlcqk9dxf4vlewslauwr8try0tl'
coin_name = 'tdel'
coin_amount = 10

tx11 = MultysigCreateTXTransaction(wallet.get_address(), sender, receiver, coin_name, coin_amount)
api.send_tx(tx11, wallet)

```

## Multisig Sign TX Transaction
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import MultysigSignTXTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")

tx_id = 'dxmstx1tqmjch2x5uk9wgnu8zl88rj6h4hy8rm8mtqfft'

tx12 = MultysigSignTXTransaction(wallet.get_address(), tx_id)
api.send_tx(tx12, wallet)

```

## Multisend Coin Transaction
```python

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
        "receiver": 'dxaa13m9gxeru45wxlcqk9dxf4vlewslauwr8try0tl',
        "coin": 'tdel',
        "amount": 50
    }
]

tx13 = MultisendCoinTransaction(wallet.get_address(), multisend)
api.send_tx(tx13, wallet)

```
## Issue Check
```python

from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI

api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
data = {
    "nonce": "34",
    "coin": "tdel",
    "amount": "100",
    "password": "123",
    "due_block": 999999999,
}

api.issue_check(wallet, data)
```

## Redeem Check
```python
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI

api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
data = {
    "check": "ERp9FR24Vz19XG....",
    "password": "123",
}

api.redeem_check(data, wallet);
```

## Mint NFT
```python
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
```

## Burn NFT
```python
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
```

## Edit NFT data
```python
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftEditMetadataTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'MyBrandNewNFT'
id = '7777'
token_uri = 'uri21'

tx3 = NftEditMetadataTransaction(denom, id, wallet.get_address(), token_uri)
api.send_tx(tx3, wallet)
```

## Transfer NFT
```python
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
```

## Delegate NFT
```python
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftDelegateTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["189", "201", "22", "30", "151", "23"]
validator_address = 'dxvaloper1mvqrrrlcd0gdt256jxg7n68e4neppu5tk872z3'

tx3 = NftDelegateTransaction(denom, id, wallet.get_address(), validator_address, sub_token_ids)
api.send_tx(tx3, wallet)
```

## Unbound NFT
```python
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftUnboundTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["201"]
validator_address = 'dxvaloper1mvqrrrlcd0gdt256jxg7n68e4neppu5tk872z3'

tx = NftUnboundTransaction(denom, id, wallet.get_address(), validator_address, sub_token_ids)
api.send_tx(tx, wallet)
```

## Update NFT reserve
```python
from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import NftUpdateReserveTransaction
wallet = Wallet("doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")

denom = 'eightbal'
id = '886688'
sub_token_ids = ["201"]
reserve = 15

tx = NftUpdateReserveTransaction(denom, id, wallet.get_address(), reserve, sub_token_ids)
api.send_tx(tx, wallet)
```