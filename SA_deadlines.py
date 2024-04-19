# import necessary modules
import random
import math
import numpy as np
import time
from scipy.stats import gamma
from ETC_Generation import *
from Helper_funcs import *

# calculate probability of accepting new makespan
def acceptance_probability(current_makespan, new_makespan, temperature):
    if new_makespan < current_makespan:
        return 1.0
    else:
        return 1 / (1 + math.exp((current_makespan - new_makespan) / temperature))

# Define the fitness function
def fitness_function(chromosome, etcMatrix, deadlines):
    machineTimes = np.zeros(len(etcMatrix[0]))
    missed_deadlines = 0
    deadline_penalty = 5000
    for i in range(len(etcMatrix)):
        machine = chromosome[i]
        task = i
        machineTimes[machine] += etcMatrix[task][machine]
        if etcMatrix[task][machine] > deadlines[i]:
            missed_deadlines += 1
    return np.max(machineTimes) + missed_deadlines * deadline_penalty


# main simulated annealing algorithm
def simulated_annealing(etc_matrix, deadlines, num_resources, initial_temperature, cooling_rate, stopping_iterations):
    num_tasks = len(etc_matrix)
    current_mapping = initial_mapping_deadlines(num_tasks, num_resources,etc_matrix,deadlines)
    best_mapping = current_mapping.copy()
    current_makespan = fitness_function(current_mapping, etc_matrix, deadlines)
    best_makespan = current_makespan
    temperature = initial_temperature
    unchanged_iterations = 0

    # iterate until stopping conditions are met or temperature reaches zero
    while unchanged_iterations < stopping_iterations and temperature > pow(10, -200):
        new_mapping = current_mapping.copy()
        random_task = random.randint(0, num_tasks - 1)
        new_resource = random.randint(0, num_resources - 1)
        while etc_matrix[random_task][new_resource] > deadlines[random_task]:
            random_task = random.randint(0, num_tasks - 1)
            new_resource = random.randint(0, num_resources - 1)
        new_mapping[random_task] = new_resource
        new_makespan = fitness_function(new_mapping, etc_matrix, deadlines)

        if new_makespan < best_makespan:
            best_mapping = new_mapping
            best_makespan = new_makespan
            unchanged_iterations = 0
        else:
            unchanged_iterations += 1
            if acceptance_probability(current_makespan, new_makespan, temperature) < random.random():

                current_mapping = new_mapping
                current_makespan = new_makespan
                unchanged_iterations = 0
        temperature *= cooling_rate

    return best_mapping, best_makespan


# define parameters
t = 1000
m = 32

average_time = 0
num_resources = m
initial_temperature = 1000000
cooling_rate = 0.99
stopping_iterations = 10000

# Call SA for each ETC, gather average makespan & time
# Low task / Low machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/LT_LM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
order, makespan = simulated_annealing(etc,deadlines,m,initial_temperature, cooling_rate, stopping_iterations)
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
