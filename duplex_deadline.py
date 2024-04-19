# import necessary modules
import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *
from min_min_deadline import *
from max_min_deadline import *


def duplex(t, m, etc, deadlines):
    #Run both min-min & max-min to obtain results
    minmin_result, Minmin_makespan = min_min(t, m, etc, deadlines)
    maxmin_result, Maxmin_makespan = max_min(t, m, etc, deadlines)

    #Determine & keep better result
    if Minmin_makespan < Maxmin_makespan:
        result = minmin_result
        makespan = Minmin_makespan
    else:
        result = maxmin_result
        makespan = Maxmin_makespan

    return result, makespan


# Call Duplex for each ETC, gather average time & each makespan
t = 1000
m = 32
average_time = 0


# Low task / Low machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/LT_LM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# Low task / Low machine heterogeneity / Partially Consistent
with open('largerDeadline_matrices/LT_LM_PartiallyConsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# Low task / Low machine heterogeneity / Consistent
with open('largerDeadline_matrices/LT_LM_Consistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# Low task / High machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/LT_HM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# Low task / High machine heterogeneity / Partially Consistent
with open('largerDeadline_matrices/LT_HM_PartiallyConsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# Low task / High machine heterogeneity / Consistent
with open('largerDeadline_matrices/LT_HM_Consistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# High task / Low machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/HT_LM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# High task / Low machine heterogeneity / Partially Consistent
with open('largerDeadline_matrices/HT_LM_PartiallyConsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# High task / Low machine heterogeneity / Consistent
with open('largerDeadline_matrices/HT_LM_Consistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# High task / High machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/HT_HM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# High task / High machine heterogeneity / Partially Consistent
with open('largerDeadline_matrices/HT_HM_PartiallyConsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

# High task / High machine heterogeneity / Consistent
with open('largerDeadline_matrices/HT_HM_Consistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = duplex(t, m, etc, deadlines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)

average_time = average_time / 12
print("Average Time:", average_time)