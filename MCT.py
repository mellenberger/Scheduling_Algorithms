# import necessary modules
import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *


def MCT(t, m, etc):
    #Initialize Variables
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    machine_times = np.zeros(m, dtype=int)
    order = np.zeros(t,  dtype=int)

    for i in range(t):
        #Choose arbitrary task to assign
        assign = np.random.choice(need_assignment)

        #Find the time it would take to execute chosen task with consideration to machine times
        task_times = machine_times + etc[assign]

        #Choose minimum completion time & assign
        I = np.argmin(task_times)
        order[assign] = I

        #Remove assigned task from unmapped list
        ind = np.argwhere(need_assignment==assign)
        need_assignment = np.delete(need_assignment, ind)

        #Update machine times based on assignment
        machine_times[I] = machine_times[I] + etc[assign][I]

    makespan = calculate_makespan(order, etc)
    return order, makespan

# Call MCT to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(100):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = MCT(t, m, etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 100
average_time = average_time / 100
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)