# Decimal Python SDK (stub)

Check out these links:
- [Decimal SDK docs](https://help.decimalchain.com/api-sdk/).
- [Decimal Console site](https://console.decimalchain.com/).

## Wallet API
### Generate new wallet
```python
from decimal_sdk import Wallet

wallet = Wallet()

```
### Generate wallet from mnemonic
```python
from decimal_sdk import Wallet

wallet = Wallet('erase august mask elevator sand picture north there apple equal anchor target')

```
### Get wallet address
```python
from decimal_sdk import Wallet

wallet = Wallet()
address = wallet.get_address()

```