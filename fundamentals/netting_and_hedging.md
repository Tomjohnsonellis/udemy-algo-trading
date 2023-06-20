# Netting vs Hedging


##### Netting
Say we are very confident in a prediction and open a large trade of BUY 100K units.
Then something happens and we are no longer as confident, so we sell 50K units.

This would leave us with (100K - 50K) = 50K units.

This is NETTING, the default behaviour on OANDA and many other exchanges, but not all so CHECK what behaviour your broker uses.

As this behaviour essentially reduces our initial trade, we only end up paying the spread once, which is nice for us.

##### Hedging

Say we are again confident in a prediction and open a large trade of BUY 100K units.
We then change our minds and we decide to SELL 100K units. 

When hedging, instead of cancelling out the previous trade, we now have two trades open, in opposite directions. We would make neither profit nor loss from these two trades as if one makes profit, the other loses that much.

As they are two separate trades, we would end up paying the spread TWICE, not good for us!

There are certain situations where hedging is appropriate, but for most cases that WE care about, NETTING is how we want our account to behave.