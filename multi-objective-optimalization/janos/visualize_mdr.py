
# importing package 
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt 
import numpy as np 
  

#FFGA = red

# HLGA = blue

# VEGA = green

# EW = orange

# create data 
fig, ax = plt.subplots()

x = np.arange(6) 
y1 = [3, 0, 0, 0, 7, 0] 
y2 = [43, 1500, 286, 0, 72, 0] 
width = 0.35
  
# plot data in grouped manner of bar type 
bar1 = plt.bar(x-0.19, y1, width) 
bar2 = plt.bar(x+0.19, y2, width) 
ax.bar_label(ax.containers[0], label_type='edge')
ax.bar_label(ax.containers[1], label_type='edge')


bar1[0].set_color('r')
bar1[1].set_color('r')
bar1[2].set_color('r')
bar1[3].set_color('b')
bar1[4].set_color('b')
bar1[5].set_color('g')

bar2[0].set_color('b')
bar2[1].set_color('g')
bar2[2].set_color('orange')
bar2[3].set_color('g')
bar2[4].set_color('orange')
bar2[5].set_color('orange')

ffga_patch = mpatches.Patch(color='red', label='FFGA')
hlga_patch = mpatches.Patch(color='blue', label='HLGA')
vega_patch = mpatches.Patch(color='green', label='VEGA')
ew_patch = mpatches.Patch(color='orange', label='EW')

plt.legend(handles=[ffga_patch, hlga_patch, vega_patch, ew_patch])

plt.xlabel("")
plt.ylabel("MDR")

plt.gca().xaxis.set_major_locator(plt.NullLocator())


plt.show()