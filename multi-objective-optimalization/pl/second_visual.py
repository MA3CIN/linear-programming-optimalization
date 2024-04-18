import pandas as pd
import matplotlib.pyplot as plt



# data
labels = ['', '', '', '', '', '']
ffga = [0,0,0,0,0,0]
hlga = [0, 0, 0, 0,0,0]
vega = [0, 1500, 0, 0,0,0]
ew = [0, 0, 289, 0,142,0]

# create a dataframe from the lists
df = pd.DataFrame([ffga, hlga, vega, ew], columns=labels, index=['', '', '', '','', ''])

# plot
p = df.plot.bar(rot=0)
plt.show()
