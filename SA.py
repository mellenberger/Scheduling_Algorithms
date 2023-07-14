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
t = 3200
m = 100
num_resources = m
initial_temperature = 1000
cooling_rate = 0.8
stopping_iterations = 200
# Call Duplex to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
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
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.6, 0.6, 1000)
    start_time = time.time()
    order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
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
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.5, 0.1, 1000)
    start_time = time.time()
    order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
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
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_2(t, m, 0.1, 0.6, 1000)
    start_time = time.time()
    order, makespan = simulated_annealing(etc,m,initial_temperature, cooling_rate, stopping_iterations)
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