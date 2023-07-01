# import necessary modules
import random
import math
import numpy as np
from ETC_Generation import *
from Helper_funcs import *
import time


#Initialize Variables
def OLB(t, m, etc):
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    machine_times = np.zeros(m, dtype=int)
    order = np.zeros(t,  dtype=int)

    for i in range(t):
        #Choose arbitrary task to assign
        assign = np.random.choice(need_assignment)

        #Find machine that will be avaible soonest & assign task to that machine
        I = np.argmin(machine_times)
        order[assign] = I

        #Remove assigned task from unmapped task list
        ind = np.argwhere(need_assignment==assign)
        need_assignment = np.delete(need_assignment, ind)

        #Update machine time availability
        machine_times[I] = machine_times[I] + etc[assign][I]

    makespan = calculate_makespan(order, etc)
    return order, makespan

# Call OLB to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(100):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = OLB(t, m, etc)
    average_makespan = average_makespan + makespan
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed

average_makespan = average_makespan / 100
average_time = average_time / 100
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)