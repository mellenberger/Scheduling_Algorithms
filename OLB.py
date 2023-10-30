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

# Call OLB for each ETC, gather average time & each makespan
t = 1000000
m = 256
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("ETC_Matrices\LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("ETC_Matrices\LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("ETC_Matrices\LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("ETC_Matrices\LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("ETC_Matrices\LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Consistent
etc = np.loadtxt("ETC_Matrices\LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("ETC_Matrices\HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("ETC_Matrices\HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Consistent
etc = np.loadtxt("ETC_Matrices\HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("ETC_Matrices\HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("ETC_Matrices\HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Consistent
etc = np.loadtxt("ETC_Matrices\HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = OLB(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)

