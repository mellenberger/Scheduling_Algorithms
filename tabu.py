import random
import numpy as np
import time
from Helper_funcs import *

def generate_neighbors(schedule, num_neighbors, etc):
    neighbors = []
    for _ in range(num_neighbors):
        i, j = random.sample(range(len(schedule)), 2)  # Select two tasks randomly
        neighbor = schedule.copy()
        neighbor[i], neighbor[j] = schedule[j], schedule[i]  # Swap the two tasks
        neighbors.append(neighbor)
    return neighbors

def tabu_search(initial_schedule, etc, max_iterations, num_neighbors):
    best_schedule = initial_schedule
    best_makespan = calculate_makespan(initial_schedule, etc)
    current_schedule = initial_schedule
    tabu_list = []
    tabu_tenure = int(np.sqrt(len(initial_schedule)))  # Tabu tenure as a function of the number of tasks

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_schedule, num_neighbors, etc)
        valid_moves = [schedule for schedule in neighbors if schedule not in tabu_list]

        if not valid_moves:
            break  # If there are no valid moves left, stop the search

        current_schedule = min(valid_moves, key=lambda x: calculate_makespan(x, etc))
        current_makespan = calculate_makespan(current_schedule, etc)

        if current_makespan < best_makespan:
            best_schedule = current_schedule
            best_makespan = current_makespan

        tabu_list.append(current_schedule)

        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0)  # Remove the oldest move from the tabu list

    return best_schedule, best_makespan


# Call Tabu for each ETC, gather average time & each makespan
num_tasks = 512
num_machines = 16
initial_schedule = initial_mapping(num_tasks, num_machines)
max_iterations = 100
num_neighbors = 50  # Number of neighbors to generate in each iteration
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Consistent
etc = np.loadtxt("LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Consistent
etc = np.loadtxt("HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Consistent
etc = np.loadtxt("HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)