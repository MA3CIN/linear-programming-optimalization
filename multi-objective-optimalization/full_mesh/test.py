import numpy as np 
import scipy.stats as st 
import statistics
# define sample data 
gfg_data = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
  
# create 99% confidence interval 
values = st.t.interval(confidence=0.90, 
              df=len(gfg_data)-1, 
              loc=np.mean(gfg_data),  
              scale=st.sem(gfg_data)) 

print(statistics.mean(gfg_data))
print(values[0])
print(values[1])
print(statistics.mean(gfg_data) - values[0])
print(values[1]- statistics.mean(gfg_data))