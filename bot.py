from coinbase.wallet.client import Client
import time
import os
from keys import API_KEY, API_SECRET, ACCOUNT_ID

client = Client(API_KEY, API_SECRET)


accounts = client.get_accounts()
assert isinstance(accounts.data, list)
assert accounts[0] is accounts.data[0]
assert len(accounts[::]) == len(accounts.data)


x = client.get_buy_price(currency_pair = 'BTC-CAD')
y = client.get_sell_price(currency_pair = 'BTC-CAD')
print(x["amount"])
s = time.strftime('%Y-%m-%d-%H-%M-%S')  #will produce 2011-10-24-13-10
print(s)


cwd = os.getcwd()
f = open( cwd + "\logs\\" + s + ".txt" , "w+")

f.write(str(x['amount']) + '\n')
f.write(str(y['amount']) + '\n')
f.write(str(s) + '\n')


#print(client.get_spot_price(currency_pair = 'BTC-CAD'))

#print(client.get_time())
#print(client.get_primary_account())


#print(client.get_transactions(ACCOUNT_ID))
