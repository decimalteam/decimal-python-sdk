from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
tx = SendCoinTransaction(wallet.get_address(), "dx13ykakvugqwzqqmqdj2j2hgqauxmftdn3kqy69g", "del", 1)
api.send_tx(tx, wallet)


from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import BuyCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
tx2 = BuyCoinTransaction(wallet.get_address(), "btc", "del", 1, 2)
api.send_tx(tx2, wallet)


from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SellAllCoinsMsgTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
tx3 = SellAllCoinsMsgTransaction(wallet.get_address(), "del", 1, "btc", 1)
api.send_tx(tx3, wallet)


from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import DelegateTransaction

wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
tx4 = DelegateTransaction(wallet.get_address(), "dxvaloper1ajytg8jg8ypx0rj9p792x32fuxyezga4dq2uk0", "del", "1")
api.send_tx(tx4, wallet)
