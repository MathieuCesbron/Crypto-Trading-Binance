import keys
from binance.client import Client

client = Client(keys.api_key, keys.secret_key)

balance_dollar = 1800
fees = 0.0015
limit_high = 1
limit_low = 0.998


def getGain(pair):
    
    count =0
    klines = client.get_historical_klines(pair, Client.KLINE_INTERVAL_1HOUR, "1 May, 2019", "1 Jun, 2019")

    for i in range( len(klines)):
        if count == 0:
            if float(klines[i][2]) > limit_high:
                count += 1
                direction = 'high'
            if float(klines[i][3]) < limit_low:
                count += 1
                direction = 'low'
            
        if count != 0:
            if float(klines[i][2]) > limit_high and direction == 'low':
                count += 1
                direction = 'high'
            if float(klines[i][3]) < limit_low and direction == 'high':
                count += 1
                direction = 'low'     
            

    gain_dollar = (limit_high - limit_low - fees)*count*balance_dollar
            
    print(count)
    print(gain_dollar)
    return(count, gain_dollar)

getGain('TUSDUSDT')
getGain('PAXUSDT')
        
