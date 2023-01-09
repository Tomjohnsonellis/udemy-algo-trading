import pandas as pd
import tpqoa

api = tpqoa.tpqoa("../data/oanda.cfg")
info = api.get_account_summary()
print("The account summary datatype is: {}".format(type(info)))
print(info)

# It's better practice to make api calls for each piece of information as needed,
# As apposed to just storing everything in memory.
# Also we will (eventually) be working with LIVE market data, we can't afford to be working with outdated information!

print("Account type: {}".format(api.account_type))
print(api.get_instruments())
# But for things like the list of instruments, that doesn't matter.
instruments = api.get_instruments()

print("There are {} different instruments, E.g. {}".format(len(instruments), instruments[0]))