import keys
from time import sleep
import datetime
from binance.client import Client


# TRADING BOT for Binance***************************************************************************************************************************

version = 1.3
client = Client(keys.api_key, keys.secret_key)
time_start = datetime.datetime.now()


# Balance of stable coins

free_USDT = float(client.get_asset_balance(asset='USDT')['free'])
free_PAX = float(client.get_asset_balance(asset='PAX')['free'])
free_TUSD = float(client.get_asset_balance(asset='TUSD')['free'])
free_USDC = float(client.get_asset_balance(asset='USDC')['free'])
free_USDS = float(client.get_asset_balance(asset='USDS')['free'])
free_all = free_USDT + free_PAX + free_TUSD + free_USDC + free_USDS

# Quantity and price to buy and sell

price_to_buy = 0.996
price_to_sell = 1.004
price_to_buy_order = 0.998
price_to_sell_order = 1.002

price_to_buy_USDS = 0.992
price_to_sell_USDS = 0.999
price_to_buy_order_USDS = 0.994
price_to_sell_order_USDS = 0.9975

quantity_to_trade_USDT = free_USDT
quantity_to_trade_PAX = free_PAX
quantity_to_trade_TUSD = free_TUSD
quantity_to_trade_USDC = free_USDC
quantity_to_trade_USDS = free_USDS

minimum_to_trade = 50

rate = 0.5
price_to_sell_big = 1.008
balance_mini_to_trade_big = 500



# Launch of the Bot*********************************************************************************************************************************

print(str(datetime.datetime.now()) + ' : Trading Bot ' + str(version) + ' Start')

def big_trade():
    free_USDT = float(client.get_asset_balance(asset='USDT')['free'])
    free_PAX = float(client.get_asset_balance(asset='PAX')['free'])
    free_TUSD = float(client.get_asset_balance(asset='TUSD')['free'])
    free_USDC = float(client.get_asset_balance(asset='USDC')['free'])
    free_USDS = float(client.get_asset_balance(asset='USDS')['free'])
        
    if max(free_USDT, free_PAX, free_TUSD, free_USDC, free_USDS) != free_USDT:
        
        if max(free_PAX, free_TUSD, free_USDC, free_USDS) == free_PAX and free_PAX > balance_mini_to_trade_big:      
         
            order = client.order_limit_sell(symbol='PAXUSDT',
                                            quantity=round(rate*float(client.get_asset_balance(asset='PAX')['free']), 2),
                                            price=price_to_sell_big)
            
        if max(free_PAX, free_TUSD, free_USDC, free_USDS) == free_TUSD and free_TUSD > balance_mini_to_trade_big:      
         
            order = client.order_limit_sell(symbol='TUSDUSDT',
                                            quantity=round(rate*float(client.get_asset_balance(asset='TUSD')['free']), 2),
                                            price=price_to_sell_big)
            
        if max(free_PAX, free_TUSD, free_USDC, free_USDS) == free_USDC and free_USDC > balance_mini_to_trade_big:      
         
            order = client.order_limit_sell(symbol='USDCUSDT',
                                            quantity=round(rate*float(client.get_asset_balance(asset='USDC')['free']), 2),
                                            price=price_to_sell_big)
            
        if max(free_PAX, free_TUSD, free_USDC, free_USDS) == free_USDS and free_USDS > balance_mini_to_trade_big:      
         
            order = client.order_limit_sell(symbol='USDSUSDT',
                                            quantity=round(rate*float(client.get_asset_balance(asset='USDS')['free']), 2),
                                            price=price_to_sell_big)

def getDollar():
    
    free_USDT = float(client.get_asset_balance(asset='USDT')['free'])
    free_PAX = float(client.get_asset_balance(asset='PAX')['free'])
    free_TUSD = float(client.get_asset_balance(asset='TUSD')['free'])
    free_USDC = float(client.get_asset_balance(asset='USDC')['free'])
    free_USDS = float(client.get_asset_balance(asset='USDS')['free'])
    free_all = free_USDT + free_PAX + free_TUSD + free_USDC + free_USDS
    
    total = 0
    if len(client.get_open_orders()) == 0:
        total = free_all
        return (total)
    else:
        for i in range(len(client.get_open_orders())):       
            total += float(client.get_open_orders()[i]['origQty'])        
        total += free_all
        return(total)


get_starting_Dollar = getDollar()


def getBenefit():
    return (round((getDollar()- get_starting_Dollar), 2))


def getPercentageBenefit():
    return (round(((getDollar()/get_starting_Dollar - 1)*100), 2))


# Bot***********************************************************************************************************************************************
    
big_trade()

# Sleep to not exceed Binance rate limits     
sleep(5)

while True:


    if float(client.get_asset_balance(asset='USDT')['free']) > minimum_to_trade:

        if price_to_buy_order > float(client.get_order_book(symbol='PAXUSDT')['asks'][0][0]):

            order = client.order_limit_buy(symbol='PAXUSDT',
                                           quantity=round(float(client.get_asset_balance(asset='USDT')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order PAX / USDT placed')

        if price_to_buy_order > float(client.get_order_book(symbol='TUSDUSDT')['asks'][0][0]):

            order = client.order_limit_buy(symbol='TUSDUSDT',
                                           quantity=round(float(client.get_asset_balance(asset='USDT')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order PAX / USDT placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDCUSDT')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDCUSDT',
                                           quantity=round(float(client.get_asset_balance(asset='USDT')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDC / USDT placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDSUSDT')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDSUSDT',
                                           quantity=round(float(client.get_asset_balance(asset='USDT')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDS / USDT placed')

        # Sleep to not exceed Binance rate limits 
        sleep(2) 
        
    if float(client.get_asset_balance(asset='PAX')['free']) > minimum_to_trade:

        if price_to_sell_order < float(client.get_order_book(symbol='PAXUSDT')['bids'][0][0]):

            order = client.order_limit_sell(symbol='PAXUSDT',
                                            quantity=round(float(client.get_asset_balance(asset='PAX')['free']), 2),
                                            price=price_to_sell)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDT / PAX placed')


        if price_to_sell_order < float(client.get_order_book(symbol='PAXTUSD')['bids'][0][0]):

            order = client.order_limit_sell(symbol='TUSDPAX',
                                            quantity=round(float(client.get_asset_balance(asset='PAX')['free']), 2),
                                            price=price_to_sell)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order TUSD / PAX placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDCPAX')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDCPAX',
                                            quantity=round(float(client.get_asset_balance(asset='PAX')['free']), 2),
                                            price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDC / PAX placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDSPAX')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDSPAX',
                                            quantity=round(float(client.get_asset_balance(asset='PAX')['free']), 2),
                                            price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDC / PAX placed')

        # Sleep to not exceed Binance rate limits 
        sleep(2)
        
    if float(client.get_asset_balance(asset='TUSD')['free']) > minimum_to_trade:

        if price_to_sell_order < float(client.get_order_book(symbol='TUSDUSDT')['bids'][0][0]):

            order = client.order_limit_sell(symbol='TUSDUSDT',
                                            quantity=round(float(client.get_asset_balance(asset='TUSD')['free']), 2),
                                            price=price_to_sell)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order TUSD / USDT placed')


        if price_to_buy_order > float(client.get_order_book(symbol='PAXTUSD')['asks'][0][0]):

            order = client.order_limit_sell(symbol='PAXTUSD',
                                            quantity=round(float(client.get_asset_balance(asset='TUSD')['free']), 2),
                                            price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order TUSD / PAX placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDCTUSD')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDCTUSD',
                                           quantity=round(float(client.get_asset_balance(asset='TUSD')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDC / TUSD placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDSTUSD')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDSTUSD',
                                           quantity=round(float(client.get_asset_balance(asset='TUSD')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDS / TUSD placed')

        # Sleep to not exceed Binance rate limits 
        sleep(2) 

    if float(client.get_asset_balance(asset='USDC')['free']) > minimum_to_trade:

        if price_to_sell_order < float(client.get_order_book(symbol='USDCUSDT')['bids'][0][0]):

            order = client.order_limit_sell(symbol='USDCUSDT',
                                            quantity=round(float(client.get_asset_balance(asset='USDC')['free']), 2),
                                            price=price_to_sell)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order USDC / USDT placed')


        if price_to_sell_order < float(client.get_order_book(symbol='USDCPAX')['bids'][0][0]):

            order = client.order_limit_sell(symbol='USDCUSDT',
                                            quantity=round(float(client.get_asset_balance(asset='USDC')['free']), 2),
                                            price=price_to_sell)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order USDC / USDT placed')


        if price_to_buy_order > float(client.get_order_book(symbol='USDSUSDC')['asks'][0][0]):

            order = client.order_limit_buy(symbol='USDSUSDC',
                                            quantity=round(float(client.get_asset_balance(asset='USDC')['free']), 2),
                                            price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order USDS / USDC placed')

        # Sleep to not exceed Binance rate limits 
        sleep(2) 
        
    if float(client.get_asset_balance(asset='USDS')['free']) > minimum_to_trade:

         if price_to_sell_order_USDS < float(client.get_order_book(symbol='USDSUSDT')['bids'][0][0]):

            order = client.order_limit_sell(symbol='USDSUSDT',
                                            quantity=round(float(client.get_asset_balance(asset='USDS')['free']), 2),
                                            price=price_to_sell_USDS)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order USDS / USDT placed')


         if price_to_sell_order_USDS < float(client.get_order_book(symbol='USDSPAX')['bids'][0][0]):

            order = client.order_limit_sell(symbol='USDSPAX',
                                            quantity=round(float(client.get_asset_balance(asset='USDS')['free']), 2),
                                            price=price_to_sell_USDS)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order USDS / PAX placed')


         if price_to_sell_order_USDS < float(client.get_order_book(symbol='USDSUSDC')['bids'][0][0]):

            order = client.order_limit_sell(symbol='USDSUSDC',
                                            quantity=round(float(client.get_asset_balance(asset='USDS')['free']), 2),
                                            price=price_to_sell_USDS)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order USDS / USDC placed')

    # Sleep to not exceed Binance rate limits 
    sleep(15)
    
    # LOG
    print(str(datetime.datetime.now()) + ' : Update')
    print(str(datetime.datetime.now()) + ' : Time since launch : ' + str(datetime.datetime.now() - time_start))
    print(str(datetime.datetime.now()) + ' : Gains since the start : ' + str(getBenefit()) + "$")
    print(str(datetime.datetime.now()) + ' : Percentage of gains : ' + str(getPercentageBenefit()) + '%')
