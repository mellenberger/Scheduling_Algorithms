# import necessary modules
import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *
from Min_Min import *
from Max_min import *


def duplex(t, m, etc):
    #Run both min-min & max-min to obtain results
    minmin_result, Minmin_makespan = min_min(t, m, etc)
    maxmin_result, Maxmin_makespan = max_min(t, m, etc)

    #Determine & keep better result
    if Minmin_makespan < Maxmin_makespan:
        result = minmin_result
        makespan = Minmin_makespan
    else:
        result = maxmin_result
        makespan = Maxmin_makespan

    return result, makespan

# Call Max-Min to run 100 times, gather average makespan & time
#High task heterogeneity low machine heterogeneity
t = 3200
m = 100
average_time = 0
average_makespan = 0

for i in range(100):
    etc = CVB_ETC_1(t, m, 0.3, 0.1, 1000)
    start_time = time.time()
    order, makespan = max_min(t,m,etc)
    end_time = time.time()
    average_time += (end_time - start_time)
    average_makespan += (makespan)

average_time = average_time/100
average_makespan = average_makespan/100

print("Average Time:", average_time)
print("Average Makespan:", average_makespan)