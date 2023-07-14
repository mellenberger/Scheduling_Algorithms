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


# Call Duplex to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = duplex(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("Low task, Low machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / high machine
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.6, 0.6, 1000)
    start_time = time.time()
    order, makespan = duplex(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("High Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / low machine
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.5, 0.1, 1000)
    start_time = time.time()
    order, makespan = duplex(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("High Task, Low Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# Low task heterogeneity high machine
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_2(t, m, 0.1, 0.6, 1000)
    start_time = time.time()
    order, makespan = duplex(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("Low Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)