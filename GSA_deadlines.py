import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *

# Genetic Algorithm parameters
populationSize = 100
numGenerations = 1500
mutationRate = 0.01
tournamentSize = 5

# Simulated Annealing parameters
initial_temperature = 1000000
cooling_rate = 0.99
stopping_iterations = 10000

# Calculate makespan for a given mapping
def calculate_makespan(mapping, etc_matrix):
    num_resources = len(np.unique(mapping))
    machine_times = np.zeros(num_resources)

    for task, resource in enumerate(mapping):
        machine_times[resource] += etc_matrix[task][resource]

    return np.max(machine_times)

# Define the fitness function
def fitness_function(chromosome, etcMatrix, deadlines):
    machineTimes = np.zeros(len(etcMatrix[0]))
    missed_deadlines = 0
    deadline_penalty = 10000
    for i in range(len(etcMatrix)):
        machine = chromosome[i]
        task = i
        machineTimes[machine] += etcMatrix[task][machine]
        if etcMatrix[task][machine] > deadlines[i]:
            missed_deadlines += 1
    return np.max(machineTimes) + missed_deadlines * deadline_penalty

def acceptance_probability(current_makespan, new_makespan, temperature):
    if new_makespan < current_makespan:
        return 1.0
    else:
        return 1 / (1 + math.exp((current_makespan - new_makespan) / temperature))

def GSA(etc_matrix, num_resources, deadlines):
    num_tasks = len(etc_matrix)
    population = np.zeros((populationSize, num_tasks), dtype=int)

    # Initialize population
    for i in range(populationSize):
        population[i] = initial_mapping_deadlines(num_tasks, num_resources,etc_matrix,deadlines)

    temperature = initial_temperature
    unchanged_iterations = 0
    current_mapping = initial_mapping_deadlines(num_tasks, num_resources, etc_matrix, deadlines)
    best_mapping = current_mapping.copy()
    current_makespan = fitness_function(current_mapping, etc_matrix,deadlines)
    best_makespan = current_makespan
    new_population = population.copy()

    for gen in range(numGenerations):
        for i in range(populationSize):
            random_task = random.randint(0, num_tasks - 1)
            new_resource = random.randint(0, num_resources - 1)
            while etc_matrix[random_task][new_resource] > deadlines[random_task]:
                random_task = random.randint(0, num_tasks - 1)
                new_resource = random.randint(0, num_resources - 1)
            new_population[i][random_task] = new_resource

        # Mutation
        for i in range(populationSize):
            for j in range(num_tasks):
                if random.random() < mutationRate:
                    new_resource = random.randint(0,num_resources-1)
                    while etc[j][new_resource] > deadlines[j]:
                        new_resource = random.randint(0,num_resources-1)
                    new_population[i][j] = new_resource

        for i in range(populationSize):
            new_mapping = new_population[i]
            new_makespan = fitness_function(new_mapping, etc_matrix,deadlines)

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

# Call GSA for each ETC, gather average makespan & time
t = 1000
m = 32
num_resources = m
average_time = 0


# Low task / Low machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/LT_LM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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
order, makespan = GSA(etc, num_resources, deadlines)
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