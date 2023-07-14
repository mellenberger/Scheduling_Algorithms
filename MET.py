# import necessary modules
import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *


def MET(t, m, etc):
    #Initialize Variables
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    order = np.zeros(t,  dtype=int)

    for i in range(t):
        #Choose arbitrary task to assign
        assign = np.random.choice(need_assignment)

        #Find machine with minimum execution time for chosen task
        I = np.argmin(etc[assign])
        order[assign] = I

        #Remove assigned task from unmapped list
        ind = np.argwhere(need_assignment==assign)
        need_assignment = np.delete(need_assignment, ind)

    makespan = calculate_makespan(order, etc)
    return order, makespan


# Call MET to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = MET(t, m, etc)
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
    order, makespan = MET(t, m, etc)
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
    order, makespan = MET(t, m, etc)
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
    order, makespan = MET(t, m, etc)
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