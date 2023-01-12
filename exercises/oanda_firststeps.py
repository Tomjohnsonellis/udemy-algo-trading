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

#####
# We can get historical price data (which we will be using to train models) like so:
help(api.get_history)
df = api.get_history(
    instrument="EUR_USD",  # The instrument we care about
    start="2020-07-01",  # Start date for data
    end="2020-07-31",  # End data for data
    granularity="D",  # Time-frame, like Day(D), 30 minutes(M30)...
    price="B"  # (B)id or (A)sk price
)

print("df column names: {}".format(df.columns))

#####
# Loading live data isn't too difficult!
# I imagine that actually using it will be...

# We can start "listening" to the stream of data like so:
api.stream_data("EUR_USD", stop=5)
# If we didn't have a timeout, we can stop like so:
api.stop_stream


