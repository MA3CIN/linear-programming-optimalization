
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
y1 = [6.1, 37.8, 2.3, 0, 0, 0.8] 
y2 = [13.7, 5.1, 5.9, 3.5, 4.2, 7.9] 
width = 0.35
  
error1 = [7.6,23.3,2.5,0,0,1.12] 
error2 = [19.9,4.2,4.1,4.9,3.8,5.1]


# plot data in grouped manner of bar type 
bar1 = plt.bar(x-0.19, y1, width) 
bar2 = plt.bar(x+0.19, y2, width) 
ax.bar_label(ax.containers[0], label_type='edge', fontweight='bold')
ax.bar_label(ax.containers[1], label_type='edge', fontweight='bold')


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

legend_properties = {'weight':'bold'}
plt.legend(handles=[ffga_patch, hlga_patch, vega_patch, ew_patch], prop=legend_properties)

plt.xlabel("")
plt.ylabel("MDR",fontweight='bold', fontsize=14)


plt.errorbar(x-0.19, y1, yerr=error1, color="black", capsize=7, ls='none')
plt.errorbar(x+0.19, y2, yerr=error2, color="black", ls='none', capsize=7)


plt.gca().xaxis.set_major_locator(plt.NullLocator())
ax.set_yticklabels(ax.get_yticks(), weight='bold')

plt.show()