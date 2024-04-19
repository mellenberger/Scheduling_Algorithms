import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *

# Genetic Algorithm parameters
populationSize = 100
numGenerations = 200
mutationRate = 0.01
tournamentSize = 5

# Simulated Annealing parameters
initial_temperature = 1000
cooling_rate = 0.8
stopping_iterations = 200

# Calculate makespan for a given mapping


def acceptance_probability(current_makespan, new_makespan, temperature):
    if new_makespan < current_makespan:
        return 1.0
    else:
        return 1 / (1 + math.exp((current_makespan - new_makespan) / temperature))

def GSA(etc_matrix, num_resources):
    num_tasks = len(etc_matrix)
    population = np.zeros((populationSize, num_tasks), dtype=int)

    # Initialize population
    for i in range(populationSize):
        population[i] = [random.randint(0, num_resources - 1) for _ in range(num_tasks)]

    temperature = initial_temperature
    unchanged_iterations = 0
    current_mapping = initial_mapping(num_tasks, num_resources)
    best_mapping = current_mapping.copy()
    current_makespan = calculate_makespan(current_mapping, etc_matrix)
    best_makespan = current_makespan
    

    for gen in range(numGenerations):
        new_population = population.copy()

        for i in range(populationSize):
            random_task = random.randint(0, num_tasks - 1)
            new_resource = random.randint(0, num_resources - 1)
            new_population[i][random_task] = new_resource

        # Mutation
        for i in range(populationSize):
            for j in range(num_tasks):
                if random.random() < mutationRate:
                    new_population[i][j] = random.randint(0,num_resources-1)

        for i in range(populationSize):
            new_mapping = new_population[i]
            new_makespan = calculate_makespan(new_mapping, etc_matrix)

            if new_makespan < best_makespan:
                best_mapping = new_mapping
                best_makespan = new_makespan
                unchanged_iterations = 0
            else:
                unchanged_iterations += 1
                if acceptance_probability(current_makespan, new_makespan, temperature) > random.random():
                    current_mapping = new_mapping
                    current_makespan = new_makespan
                    unchanged_iterations = 0

        temperature *= cooling_rate

    return best_mapping, best_makespan

# Call GSA for each ETC, gather average makespan & time
t = 15
m = 3
num_resources = m
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("QUBO_matrices\LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("QUBO_matrices\LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("QUBO_matrices\LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine / Inconsistent
etc = np.loadtxt("QUBO_matrices\LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine / Partially Consistent
etc = np.loadtxt("QUBO_matrices\LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine / Consistent
etc = np.loadtxt("QUBO_matrices\LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine / Inconsistent
etc = np.loadtxt("QUBO_matrices\HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine / Partially consistent
etc = np.loadtxt("QUBO_matrices\HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine / Consistent
etc = np.loadtxt("QUBO_matrices\HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine / Inconsistent
etc = np.loadtxt("QUBO_matrices\HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine / Partially consistent
etc = np.loadtxt("QUBO_matrices\HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine / Consistent
etc = np.loadtxt("QUBO_matrices\HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = GSA(etc, num_resources)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)