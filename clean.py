import keys
from time import sleep
import datetime
from binance.client import Client


# TRADING BOT for Binance***************************************************************************************************************************

version = 1.0
client = Client(keys.api_key, keys.secret_key)
time_start = datetime.datetime.now()


# Launch of the Bot*********************************************************************************************************************************

print(str(datetime.datetime.now()) + ' : Trading Bot ' + str(version) + ' Start')

# Variables*****************************************************************************************************************************************

minimum_to_trade = 10
price_to_buy = 0.998
price_to_sell = 1.002

# Benefit*******************************************************************************************************************************************

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




while True:
    
    if float(client.get_asset_balance(asset='USDT')['free']) > minimum_to_trade:

            order = client.order_limit_buy(symbol='TUSDUSDT',
                                           quantity=round(float(client.get_asset_balance(asset='USDT')['free']), 2),
                                           price=price_to_buy)

            print(str(datetime.datetime.now()) + ' : Limit Buy Order PAX / USDT placed')
            
    if float(client.get_asset_balance(asset='TUSD')['free']) > minimum_to_trade:
        
            order = client.order_limit_sell(symbol='TUSDUSDT',
                                           quantity=round(float(client.get_asset_balance(asset='TUSD')['free']), 2),
                                           price=price_to_sell)

            print(str(datetime.datetime.now()) + ' : Limit Sell Order PAX / USDT placed')
            
    # Sleep to not exceed Binance rate limits 
    sleep(10)
    
    # LOG
    print(str(datetime.datetime.now()) + ' : Update')
    print(str(datetime.datetime.now()) + ' : Time since launch : ' + str(datetime.datetime.now() - time_start))
    print(str(datetime.datetime.now()) + ' : Gains since the start : ' + str(getBenefit()) + "$")
    print(str(datetime.datetime.now()) + ' : Percentage of gains : ' + str(getPercentageBenefit()) + '%')
    
    # Sleep to not exceed Binance rate limits 
    sleep(10)
    