import heapq
import numpy as np
import time
import numpy as np
from ETC_Generation import *

MAX_NODES = 1024


class Node:
    def __init__(self, mapping, remaining_tasks, machine_availability_times, etc_matrix):
        self.mapping = mapping
        self.remaining_tasks = remaining_tasks
        self.machine_availability_times = machine_availability_times
        self.makespan = max(machine_availability_times)
        if remaining_tasks:
            self.h1 = calculate_h1(remaining_tasks, etc_matrix)
            self.h2 = calculate_h2(remaining_tasks, machine_availability_times, etc_matrix)
            self.cost = self.makespan + self.h1 + self.h2
        else:
            self.h1 = 0
            self.h2 = 0
            self.cost = self.makespan + self.h1 + self.h2

    def __lt__(self, other):
        return self.cost < other.cost



def calculate_h1(remaining_tasks, etc_matrix):
    if not remaining_tasks:
        return 0
    min_times = [min(etc_matrix[task]) for task in remaining_tasks]
    return max(min_times)


def calculate_h2(remaining_tasks, machine_availability_times, etc_matrix):
    if not remaining_tasks:
        return 0
    makespan = max(machine_availability_times)
    sdma = sum(makespan - mat for mat in machine_availability_times if mat < makespan)
    smet = sum(min(etc_matrix[task]) for task in remaining_tasks)
    return max(smet - sdma, 0)


def generate_etc(num_tasks, num_machines):
    # Use numpy to generate a matrix of random values
    etc_matrix = np.random.rand(num_tasks, num_machines)

    # Multiply by a factor if you want the values to be in a certain range, e.g., 0 to 100
    etc_matrix *= 100

    return etc_matrix

def a_star_search(etc_matrix, num_resources):
    num_tasks = len(etc_matrix)
    initial_mapping = [-1] * num_tasks
    initial_machine_availability_times = [0] * num_resources
    initial_remaining_tasks = set(range(num_tasks))

    initial_node = Node(initial_mapping, initial_remaining_tasks, initial_machine_availability_times, etc_matrix)
    open_list = []
    heapq.heappush(open_list, initial_node)

    while open_list:
        while len(open_list) > MAX_NODES:
            # Prune the nodes by removing the one with maximum cost
            max_node = max(open_list, key=lambda node: node.cost)
            open_list.remove(max_node)
            heapq.heapify(open_list)

        current_node = heapq.heappop(open_list)
        if not current_node.remaining_tasks:
            return current_node.mapping, current_node.makespan

        current_mapping = current_node.mapping.copy()
        current_machine_availability_times = current_node.machine_availability_times.copy()
        current_remaining_tasks = current_node.remaining_tasks.copy()

        #for task in current_remaining_tasks:
        task = list(current_remaining_tasks)[0]
        new_node = [-1] * num_resources
        for machine in range(num_resources):
            new_mapping = current_mapping.copy()
            new_mapping[task] = machine
            new_machine_availability_times = current_machine_availability_times.copy()
            new_machine_availability_times[machine] += etc_matrix[task][machine]
            new_remaining_tasks = current_remaining_tasks.copy()
            new_remaining_tasks.remove(task)

            new_node[machine] = Node(new_mapping, new_remaining_tasks, new_machine_availability_times, etc_matrix)
        
        lowest_cost_node = min(range(num_resources), key=lambda i: new_node[i].makespan)
        heapq.heappush(open_list, new_node[lowest_cost_node])

    return None



# Call A* for each ETC, gather average time & each makespan
t = 15
m = 3
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("QUBO_matrices/LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("QUBO_matrices/LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("QUBO_matrices/LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("QUBO_matrices/LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("QUBO_matrices/LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Consistent
etc = np.loadtxt("QUBO_matrices/LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("QUBO_matrices/HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("QUBO_matrices/HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Consistent
etc = np.loadtxt("QUBO_matrices/HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("QUBO_matrices/HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("QUBO_matrices/HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Consistent
etc = np.loadtxt("QUBO_matrices/HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = a_star_search(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)

