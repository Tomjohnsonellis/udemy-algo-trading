"""
This is a little exercise to get familiar with time series data,
the data used here is the temperatures of Los Angeles and New York over 3 years.
"""

import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("../course content/Part2_Materials/Video_Lecture_NBs/temp.csv",
                   parse_dates=["datetime"],
                   index_col="datetime")

# print(dataset.head())
print(dataset.columns)

# The .loc operator is very useful for slicing time-series data.
# We can perform "label based indexing"
# For example, if I just want June 2014

print(dataset.loc["2014-06"])
data = dataset.loc["2014-06"]

x = data.index
y = data["LA"]
z = data["NY"]

fig, ax = plt.subplots()
ax.plot(x, y, z)
plt.savefig("temps_over_time.png")
# Not the prettiest graph I've made,
# I can make nicer ones with R but I'm sure matplotlib CAN make pretty graphs
plt.show()

