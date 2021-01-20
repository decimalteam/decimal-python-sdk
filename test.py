from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import SendCoinTransaction
wallet = Wallet("hollow luggage slice soup leg vague icon walnut session candy improve struggle")
api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
tx2 = SendCoinTransaction(wallet.get_address(), "dx1xre7cdvkmqg848tyxeyl657q0nc6tqmtmceyv6", "tdel", 1)
api.send_tx(tx2, wallet)
