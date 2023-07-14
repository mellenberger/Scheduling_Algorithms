import heapq
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *


# represent a node in the A* search tree
class Node:
    def __init__(self, mapping, cost, makespan, remaining_tasks):
        self.mapping = mapping
        self.cost = cost
        self.makespan = makespan
        self.remaining_tasks = remaining_tasks

    # enable comparison of nodes based on their cost
    def __lt__(self, other):
        return self.cost < other.cost


# main A* algorithm
def a_star(etc_matrix, num_resources):
    num_tasks = len(etc_matrix)
    initial_mapping = [-1] * num_tasks
    open_list = []
    closed_list = set()

    initial_node = Node(initial_mapping, 0, 0, set(range(num_tasks)))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if not current_node.remaining_tasks:
            return current_node.mapping, current_node.makespan

        current_mapping = current_node.mapping
        current_makespan = current_node.makespan
        current_cost = current_node.cost

        closed_list.add(tuple(current_mapping))

        for task in current_node.remaining_tasks:
            for resource in range(num_resources):
                new_mapping = current_mapping.copy()
                new_mapping[task] = resource

                if tuple(new_mapping) in closed_list:
                    continue

                new_makespan = calculate_makespan(new_mapping, etc_matrix)
                new_cost = new_makespan + len(current_node.remaining_tasks) - 1

                new_node = Node(new_mapping, new_cost, new_makespan, current_node.remaining_tasks - {task})

                heapq.heappush(open_list, new_node)

    return None


# Call A* to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 516
m = 32
average_makespan = 0
average_time = 0
average = 2
for i in range(2):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = a_star(etc, m)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)
    if order is None:
        print("No valid mapping found.")
        average -= 1

average_makespan = average_makespan / average
average_time = average_time / average
print("Low task, Low machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / high machine
average_makespan = 0
average_time = 0
average = 2
for i in range(2):
    etc = CVB_ETC_1(t, m, 0.6, 0.6, 1000)
    start_time = time.time()
    order, makespan = a_star(etc, m)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)
    if order is None:
        print("No valid mapping found.")
        average -= 1

average_makespan = average_makespan / average
average_time = average_time / average
print("High Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / low machine
average_makespan = 0
average_time = 0
average = 2
for i in range(2):
    etc = CVB_ETC_1(t, m, 0.5, 0.1, 1000)
    start_time = time.time()
    order, makespan = a_star(etc, m)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)
    if order is None:
        print("No valid mapping found.")
        average -= 1

average_makespan = average_makespan / average
average_time = average_time / average
print("High Task, Low Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# Low task heterogeneity high machine
average_makespan = 0
average_time = 0
average = 2
for i in range(2):
    etc = CVB_ETC_2(t, m, 0.1, 0.6, 1000)
    start_time = time.time()
    order, makespan = a_star(etc, m)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)
    if order is None:
        print("No valid mapping found.")
        average -= 1

average_makespan = average_makespan / average
average_time = average_time / average
print("Low Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)