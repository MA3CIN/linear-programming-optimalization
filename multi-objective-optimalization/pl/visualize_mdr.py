
# importing package 
import matplotlib.pyplot as plt 
import numpy as np 
  
# create data 
x = np.arange(5) 
y1 = [34, 56, 12, 89, 67] 
y2 = [12, 56, 78, 45, 90] 
width = 0.40
  
# plot data in grouped manner of bar type 
plt.bar(x-0.225, y1, width) 
plt.bar(x+0.225, y2, width) 


x_labels = [
    1,2,3,4,5,6,7,8,9,10
]

# plt.set_xticklabels(x_labels)

# https://stackoverflow.com/questions/47838680/matplotlib-xticks-values-in-bar-chart

plt.xlabel("Average Pulse")
plt.ylabel("MDR")


plt.show()