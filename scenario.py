from decimal_sdk import Wallet
from decimal_sdk import DecimalAPI
from decimal_sdk import CreateCoinTransaction, SellAllCoinsMsgTransaction, SendCoinTransaction

# mnemo = "hollow luggage slice soup leg vague icon walnut session candy improve struggle"
# mnemo = "doctor transfer mystery electric any satisfy crop pill wet music legend hero success lock item dune shiver mesh badge orbit correct february rifle museum"
# mnemo = "exotic favorite initial tank bridge tuition broken hope sniff tiny fringe ice letter joke goddess skate raw similar link knife cable today table gain"
# mnemo = "assume claim blind pony crane total glance hockey reform sentence brand tide decide solid party afford year oak fortune educate else remove vapor extend"
# mnemo = "horror hope bird tray kiss write intact lady hammer mix foil mimic cupboard turtle reason volcano paddle goat tennis faculty valid swift blouse learn"
# api = DecimalAPI("https://devnet-gate.decimalchain.com/api")
#
mnemo = "eight night small joke salon catalog walk text left maze allow loyal fork talk mad tortoise dumb record broccoli bachelor genre little ordinary message"
api = DecimalAPI("https://mainnet-gate.decimalchain.com/api")
wallet = Wallet(mnemo)
print(wallet.get_address())

# title = "totally awesome coin"
# symbol = "ttlwsmcn"
# crr = "10"
# initial_reserve = "10000000000000000000000"
# initial_volume = "500000000000000000000000"
# limit_volume = "1000000000000000000000000"
# identity = 'e353b89e0de0a78974f9ecaf033721ac'
#
# tx3 = CreateCoinTransaction(wallet.get_address(), title, symbol, crr, initial_volume,
#                             initial_reserve, identity, limit_volume)
# api.send_tx(tx3, wallet)

############################################################################################################

# receiver = "dx17hecfd2t95gvhx38w76t4uvt092hyrhkz5hgsg"
# coin_name = "ttlwsmcn"
# coin_amount = 98000
# options = {
#     "denom": coin_name,
#     "memo": "message to send with transaction"
# }
# tx = SendCoinTransaction(wallet.get_address(), receiver, coin_name, coin_amount)
# api.send_tx(tx, wallet, options)

############################################################################################################

# coin_to_sell_name = "ttlwsmcn"
# coin_to_sell_amount = 0
# min_coin_to_buy_name = "del"
# min_coin_to_buy_amount = 0
# price = api.get_coin_price('ttlwsmcn')

coin_to_sell_name = "btt"
coin_to_sell_amount = 0
min_coin_to_buy_name = "del"
min_coin_to_buy_amount = 0
price = api.get_coin_price('btt')

# print(price)
# min_coin_to_buy_amount = int(float(coin_to_sell_amount) * price)
# print(min_coin_to_buy_amount)
tx4 = SellAllCoinsMsgTransaction(wallet.get_address(), coin_to_sell_name, coin_to_sell_amount,
                                 min_coin_to_buy_name, min_coin_to_buy_amount)
res = api.send_tx(tx4, wallet)
print(res)
print(tx4)

print(tx4.message.__dict__())