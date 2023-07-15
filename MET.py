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


# Call MET for each ETC, gather average time & each makespan
t = 512
m = 16
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Consistent
etc = np.loadtxt("LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Consistent
etc = np.loadtxt("HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Consistent
etc = np.loadtxt("HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = MET(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)