import json

from .wallet import Wallet
from .api import DecimalAPI
from .transactions import SendCoinTransaction
from decimal_sdk.utils.helpers import get_amount_uni


def SendAllCoin(api: DecimalAPI, wallet: Wallet, receiver: str, coin_name: str, options = {}):
    ''' Send all coins from wallet '''

    try:
        wallet_data = json.loads(api.get_address(wallet.get_address()))
        balance = '0'
        if wallet_data["ok"]:
            balance = int(wallet_data["result"]["address"]["balance"][coin_name])

        balance = int(get_amount_uni(balance, True))
        tx = SendCoinTransaction(wallet.get_address(), receiver, coin_name, balance)
        commission = api.estimate_tx_fee(tx, wallet, options)
        tx = SendCoinTransaction(wallet.get_address(), receiver, coin_name, balance - commission)
        print(tx.signer.__dict__())
        return api.send_tx(tx, wallet, options)

    except Exception as e:
        return str(e)