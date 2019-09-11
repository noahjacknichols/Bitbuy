from coinbase.wallet.client import Client


client = Client(API_KEY, API_SECRET)


accounts = client.get_accounts()
assert isinstance(accounts.data, list)
assert accounts[0] is accounts.data[0]
assert len(accounts[::]) == len(accounts.data)


print(client.get_buy_price(currency_pair = 'BTC-CAD'))
print(client.get_sell_price(currency_pair = 'BTC-CAD'))
print(client.get_spot_price(currency_pair = 'BTC-CAD'))

print(client.get_time())
print(client.get_primary_account())


print(client.get_transactions(ACCOUNT_ID))
