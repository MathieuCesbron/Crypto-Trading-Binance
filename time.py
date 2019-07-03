import time
import keys
import datetime

from binance.client import Client
client = Client(keys.api_key, keys.secret_key)
print(int(time.time() * 1000) - client.get_server_time()['serverTime'])

time_start = datetime.datetime.now()
print(time_start)

while True:
    print(datetime.datetime.now() - time_start)