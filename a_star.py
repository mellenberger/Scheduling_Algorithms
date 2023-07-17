import heapq
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *


# represent a node in the A* search tree
class Node:
    def __init__(self, mapping, cost, makespan, remaining_tasks, cost_so_far):
        self.mapping = mapping
        self.cost = cost
        self.makespan = makespan
        self.remaining_tasks = remaining_tasks
        self.cost_so_far = cost_so_far

    # enable comparison of nodes based on their cost
    def __lt__(self, other):
        return self.cost < other.cost

# main A* algorithm
def a_star(etc_matrix, num_resources):
    num_tasks = len(etc_matrix)
    initial_mapping = [-1] * num_tasks
    open_list = []
    visited = set()

    initial_node = Node(initial_mapping, 0, 0, set(range(num_tasks)), 0)
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if not current_node.remaining_tasks:
            return current_node.mapping, current_node.makespan

        current_mapping = current_node.mapping
        current_makespan = current_node.makespan
        current_cost = current_node.cost

        mapping_hash = hash(tuple(current_mapping))

        if mapping_hash in visited:
            continue

        visited.add(mapping_hash)

        for task in current_node.remaining_tasks:
            for resource in range(num_resources):
                new_mapping = current_mapping.copy()
                new_mapping[task] = resource

                new_makespan = calculate_makespan(new_mapping, etc_matrix)
                new_cost_so_far = current_node.cost_so_far + etc_matrix[task][resource]
                estimated_remaining_cost = (len(current_node.remaining_tasks) - 1) * max(etc_matrix[task])

                new_cost = new_makespan + new_cost_so_far + estimated_remaining_cost

                new_node = Node(
                    new_mapping,
                    new_cost,
                    new_makespan,
                    current_node.remaining_tasks - {task},
                    new_cost_so_far
                )

                heapq.heappush(open_list, new_node)

    return None


# Call A* for each ETC, gather average time & each makespan
t = 512
m = 16
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Consistent
etc = np.loadtxt("LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Consistent
etc = np.loadtxt("HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Consistent
etc = np.loadtxt("HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = a_star(etc, m)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)

