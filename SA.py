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


# main simulated annealing algorithm
def simulated_annealing(etc_matrix, num_resources, initial_temperature, cooling_rate, stopping_iterations):
    num_tasks = len(etc_matrix)
    current_mapping = initial_mapping(num_tasks, num_resources)
    best_mapping = current_mapping.copy()
    current_makespan = calculate_makespan(current_mapping, etc_matrix)
    best_makespan = current_makespan
    temperature = initial_temperature
    unchanged_iterations = 0

    # iterate until stopping conditions are met or temperature reaches zero
    while unchanged_iterations < stopping_iterations and temperature > pow(10, -200):
        new_mapping = current_mapping.copy()
        random_task = random.randint(0, num_tasks - 1)
        new_resource = random.randint(0, num_resources - 1)
        new_mapping[random_task] = new_resource
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


# define parameters
t = 512
m = 16
average_time = 0
num_resources = m
initial_temperature = 1000
cooling_rate = 0.8
stopping_iterations = 200

# Call SA for each ETC, gather average makespan & time
# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine / Inconsistent
etc = np.loadtxt("HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine / Partially consistent
etc = np.loadtxt("HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine / Consistent
etc = np.loadtxt("HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine / Inconsistent
etc = np.loadtxt("HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine / Partially consistent
etc = np.loadtxt("HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine / Consistent
etc = np.loadtxt("HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine / Inconsistent
etc = np.loadtxt("LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine / Partially Consistent
etc = np.loadtxt("LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine / Consistent
etc = np.loadtxt("LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)