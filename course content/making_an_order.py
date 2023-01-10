import pandas as pd
import tpqoa

# Set up our API token
api = tpqoa.tpqoa("../data/oanda.cfg")

# Remember, helpful documentation does exist!
# help(api.create_order)
api.create_order(
    instrument = "EUR_USD",
    units = 1000, # Can be negative to do a sell order!
    sl_distance = 0.1
)
# No idea how to close orders via API yet, remember to close any you make during testing!

acc_sum = api.get_account_summary()
print(type(acc_sum))
print(len(acc_sum))
for i in acc_sum:
    print(i, " ----- ", acc_sum[i])
# Print all transactions
#api.print_transactions()
# Just from an ID onwards
api.print_transactions(tid=87)