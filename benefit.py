import keys
from time import sleep
import datetime
from binance.client import Client

client = Client(keys.api_key, keys.secret_key)


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
