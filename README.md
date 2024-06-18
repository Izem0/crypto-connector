# Crypto-connector

This is a lightweight library that works as a connector to Binance, Bybit and HTX SPOT APIs.

- Supported APIs:
    - [Binance SPOT API](https://developers.binance.com/docs/binance-spot-api-docs/rest-api)
    - [Bybit SPOT API](https://bybit-exchange.github.io/docs/v5/intro)
    - [HTX SPOT API](https://www.htx.com/en-in/opend/newApiPages/)

## Installation

```bash
pip install crypto-connector
```

## Usage examples

### Public endpoints
```python
import crypto_connector as cc

exc = cc.Binance()
# exc = cc.Bybit()
# exc = cc.HTX()

# get server time
print(exc.get_server_time())

# get last 200 klines of ETHUSDT with 1d timeframe
print(exc.klines("ETHUSDT", "1d"))
```

### Private endpoints
API key/secret are required for private endpoints.
```python
import crypto_connector as cc

# some binance API endpoints require both sub and master accounts API key/secret. Therefore user needs to create a subaccount and provide subaccount api key, subaccount api_secret, subaccount email, master account api key and master account api secret to the Binance constructor
exc = cc.Binance(
    sub_api_key="",
    sub_api_secret="",
    sub_email="",
    master_api_key="",
    master_api_secret="",
)
# bybit = cc.Bybit(
#     api_key="",
#     api_secret="",
# )
# htx = cc.HTX(
#     api_key="",
#     api_secret="",
# )

# get api key info
print(exc.get_api_key_info())

# get balance
print(exc.get_balance())

# post a new order
order = exc.place_order("ETHUSDT", type="limit", side="buy", qty=0.015, price=1000)
print(order)

# get open orders
print(exc.get_open_orders())
```

## Limitation

- This library is not intended to be comprehensive, I use it mainly for my personal projects
- Not all endpoints rfor the different APIs ae supported
- Websocket and Futures are not supported