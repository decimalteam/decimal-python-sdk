from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
tx2 = SendCoinTransaction(wallet.get_address(), "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g", "del", 1)
api.send_tx(tx2, wallet)


from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("grant trust else animal manual cart wait hand taste obvious indicate swarm judge witness split choose obtain label trial home oil snake dwarf cost")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
tx2 = SendCoinTransaction(wallet.get_address(), "dx1xre7cdvkmqg848tyxeyl657q0nc6tqmtmceyv6", "del", 1)
api.send_tx(tx2, wallet)


from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SellAllCoinsMsgTransaction
wallet = Wallet("grant trust else animal manual cart wait hand taste obvious indicate swarm judge witness split choose obtain label trial home oil snake dwarf cost")
api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
tx3 = SellAllCoinsMsgTransaction(wallet.get_address(), "del", "1", "btc", "1")
api.send_tx(tx3, wallet)


from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction

api = DecimalAPI("https://testnet-gate.decimalchain.com/api")
wallet = Wallet("grant trust else animal manual cart wait hand taste obvious indicate swarm judge witness split choose obtain label trial home oil snake dwarf cost")
tx2 = SendCoinTransaction(wallet.get_address(), "dx1xre7cdvkmqg848tyxeyl657q0nc6tqmtmceyv6", "del", 1)
api.send_tx(tx2, wallet)
