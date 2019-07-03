import keys
from time import sleep
from binance.client import Client

client = Client(keys.api_key, keys.secret_key)

# Quantity and price to buy and sell

quantity_to_buy = 100
quantity_to_sell = 100
price_to_buy = 0.995
price_to_sell = 1.05

# Balance of stable coins

free_USDT = client.get_asset_balance(asset='USDT')['free']
free_TUSD = client.get_asset_balance(asset='TUSD')['free']
free_USDC = client.get_asset_balance(asset='USDC')['free']
free_USDS = client.get_asset_balance(asset='USDS')['free']

# Bid and Ask

bid_PAXUSDT = client.get_order_book(symbol='PAXUSDT')['bids'][0][0]
ask_PAXUSDT = client.get_order_book(symbol='PAXUSDT')['asks'][0][0]

bid_TUSDUSDT = client.get_order_book(symbol='TUSDUSDT')['bids'][0][0]
ask_TUSDUSDT = client.get_order_book(symbol='TUSDUSDT')['asks'][0][0]

bid_USDCUSDT = client.get_order_book(symbol='USDCUSDT')['bids'][0][0]
ask_USDCUSDT = client.get_order_book(symbol='USDCUSDT')['asks'][0][0]

bid_USDSUSDT = client.get_order_book(symbol='USDCUSDT')['bids'][0][0]
ask_USDSUSDT = client.get_order_book(symbol='USDCUSDT')['asks'][0][0]

bid_PAXTUSD = client.get_order_book(symbol='PAXTUSD')['bids'][0][0]
ask_PAXTUSD = client.get_order_book(symbol='PAXTUSD')['asks'][0][0]

bid_USDCPAX = client.get_order_book(symbol='USDCPAX')['bids'][0][0]
ask_USDCPAX = client.get_order_book(symbol='USDCPAX')['asks'][0][0]

bid_USDSPAX = client.get_order_book(symbol='USDSPAX')['bids'][0][0]
ask_USDSPAX = client.get_order_book(symbol='USDSPAX')['asks'][0][0]

bid_USDSUSDC = client.get_order_book(symbol='USDSUSDC')['bids'][0][0]
ask_USDSUSDC = client.get_order_book(symbol='USDSUSDC')['asks'][0][0]

#Data

minimum_to_trade = 100
margin = 0.01
state = "NothingPAXUSDT"
quantity_to_trade = 100

'''
order = client.order_limit_sell(symbol='USDSUSDT',
                                quantity=quantity_to_trade,
                                price=round(float(client.get_order_book(symbol='USDSUSDT')['bids'][0][0]) + margin,4))
'''

orders = client.get_all_orders(symbol='USDSUSDT', limit=10)
aytaille = len(client.get_open_orders())            
#aya = client.get_open_orders()[0]['origQty']

         