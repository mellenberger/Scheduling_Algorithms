import heapq
import random
import time
import numpy as np
from Helper_funcs import *


MAX_NODES = 10


class Node:
    def __init__(self, mapping, g_cost, h_cost, level):
        self.mapping = mapping
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.level = level

    def __lt__(self, other):
        return self.f_cost < other.f_cost


# Example Heuristic function based on the description
def calculate_h(n, max_min_RC, g_cost):
    return max(0, max_min_RC - g_cost)


# DRP A-Star algorithm
def drp_a_star(Ci, si, Sk, strategy="SA1", R=10):
    OPEN = []
    num_tasks = len(Ci)
    num_machines = len(Ci[0])

    # Initial state (all tasks are unassigned)
    initial_mapping = [-1] * num_tasks
    initial_g_cost = 0
    initial_h_cost = 0
    initial_node = Node(initial_mapping, initial_g_cost, initial_h_cost, level=0)
    heapq.heappush(OPEN, initial_node)

    iteration = 0

    while OPEN:
        # Limit the number of nodes to prevent memory overflow
        if len(OPEN) > MAX_NODES:
            OPEN = heapq.nsmallest(MAX_NODES, OPEN)
        print(len(OPEN))

        current_node = heapq.heappop(OPEN)

        # Assuming a goal state is one where all tasks are assigned
        if all(map(lambda x: x != -1, current_node.mapping)):
            return current_node.mapping

        # Generate successors
        successors = []

        for task in range(num_tasks):
            for machine in range(num_machines):
                if current_node.mapping[task] != -1:
                    continue  # Skip already assigned tasks

                new_mapping = current_node.mapping.copy()
                new_mapping[task] = machine

                # Update g_cost (cost so far)
                new_g_cost = current_node.g_cost + Ci[task][machine]

                unassigned_tasks = [i for i in range(num_tasks) if new_mapping[i] == -1]
                if unassigned_tasks:
                    max_min_RC = min([min(Ci[i]) for i in unassigned_tasks])
                    new_h_cost = calculate_h(new_mapping, max_min_RC, new_g_cost)
                else:
                    new_h_cost = 0  # or some other default value

                new_node = Node(new_mapping, new_g_cost, new_h_cost, current_node.level + 1)
                successors.append(new_node)

        # SA1 strategy: only keep the best successor at level R or below
        if strategy == "SA1":
            best_successor = min(successors, key=lambda x: x.f_cost, default=None)
            if best_successor:
                heapq.heappush(OPEN, best_successor)
            #continue

        # SA2 strategy: keep only the minimum-cost node at the first time level R is reached
        elif strategy == "SA2" and current_node.level == R:
            best_successor = min(successors, key=lambda x: x.f_cost, default=None)
            if best_successor:
                heapq.heappush(OPEN, best_successor)
            #continue

        # SA3 strategy: insert all nodes but then remove n-1 highest cost nodes at level R
        elif strategy == "SA3" and current_node.level == R:
            for successor in successors:
                heapq.heappush(OPEN, successor)
            OPEN = heapq.nsmallest(1, OPEN)
            #continue

        # Normal A* successor insertion
        elif strategy == "":
            for successor in successors:
                heapq.heappush(OPEN, successor)

        iteration += 1
        #if iteration % 500 == 0:
        print(f"Iteration {iteration}, OPEN size: {len(OPEN)}")


# Simulated Ci matrix (512 tasks, 16 machines)
Ci = [[random.randint(50, 150) for _ in range(3)] for _ in range(30)]
etc = np.loadtxt("LT_LM_Inconsistent.txt")
#order = [10, 14, 0, 11, 4, 8, 6, 2, 12, 15, 8, 12, 5, 7, 5, 7, 10, 6, 11, 10, 3, 0, 11, 0, 11, 6, 8, 7, 11, 5, 6, 13, 2, 8, 14, 6, 15, 9, 12, 12, 13, 0, 11, 15, 3, 13, 12, 8, 2, 12, 9, 14, 2, 14, 2, 7, 1, 11, 13, 14, 1, 5, 1, 5, 4, 5, 11, 14, 2, 10, 10, 10, 15, 8, 12, 6, 6, 6, 4, 2, 8, 4, 9, 6, 4, 12, 14, 10, 2, 5, 6, 10, 14, 7, 2, 12, 5, 2, 2, 6, 6, 3, 7, 5, 7, 14, 11, 4, 6, 10, 6, 12, 8, 13, 1, 0, 3, 8, 7, 13, 9, 14, 14, 7, 6, 0, 6, 1, 6, 14, 12, 3, 5, 4, 11, 8, 12, 12, 13, 7, 0, 15, 11, 9, 3, 12, 5, 3, 2, 15, 11, 6, 9, 13, 10, 1, 1, 14, 3, 9, 6, 14, 15, 3, 2, 2, 3, 4, 7, 6, 4, 5, 4, 11, 11, 1, 3, 10, 12, 6, 9, 0, 10, 1, 9, 15, 13, 11, 11, 1, 8, 4, 3, 5, 11, 10, 10, 4, 5, 7, 7, 8, 12, 15, 8, 9, 10, 9, 14, 1, 11, 8, 0, 14, 10, 8, 7, 0, 7, 8, 14, 10, 9, 9, 15, 0, 14, 3, 11, 10, 4, 14, 15, 12, 7, 8, 8, 9, 10, 4, 2, 14, 1, 8, 14, 14, 12, 6, 2, 8, 1, 10, 5, 14, 10, 12, 11, 9, 6, 6, 4, 13, 4, 11, 11, 10, 13, 15, 11, 6, 1, 1, 10, 9, 9, 9, 11, 10, 6, 7, 12, 5, 6, 15, 15, 15, 4, 7, 6, 15, 4, 3, 1, 5, 2, 9, 11, 2, 11, 2, 11, 13, 6, 15, 9, 10, 9, 9, 7, 12, 14, 13, 9, 12, 11, 4, 2, 8, 3, 2, 0, 12, 7, 0, 5, 2, 12, 13, 15, 15, 15, 13, 13, 9, 6, 2, 3, 12, 9, 6, 11, 14, 3, 15, 2, 12, 5, 15, 13, 11, 1, 9, 7, 7, 12, 15, 8, 3, 0, 12, 11, 14, 13, 10, 12, 7, 7, 7, 7, 7, 15, 7, 10, 11, 12, 15, 11, 6, 13, 2, 11, 3, 0, 9, 0, 15, 13, 0, 7, 15, 9, 6, 6, 9, 12, 1, 8, 15, 3, 1, 0, 12, 10, 3, 11, 11, 2, 9, 3, 6, 4, 12, 5, 8, 0, 0, 1, 14, 9, 9, 10, 6, 14, 2, 1, 9, 2, 3, 3, 3, 3, 3, 11, 10, 15, 14, 11, 9, 3, 6, 14, 3, 15, 11, 14, 3, 13, 7, 3, 6, 7, 1, 6, 6, 11, 5, 11, 11, 15, 14, 6, 3, 3, 1, 5, 8, 0, 11, 15, 6, 5, 3, 7, 0, 2, 2, 3, 4, 1, 1, 4, 7, 14, 12, 11, 8, 11, 14, 3, 8, 7, 8, 15, 12, 11, 6, 10, 11, 15, 10, 9, 8, 12, 6, 1, 11, 10, 15, 10, 1, 3, 9]
#makespan = calculate_makespan(order, etc)
#print(makespan)
# Simulated si array (512 tasks)
si = [1 for _ in range(128)]
# Simulated Sk array (16 machines)
Sk = [100 for _ in range(16)]
start_time = time.time()
final_mapping = drp_a_star(etc, si, Sk, strategy="SA2", R=10)
print("Final mapping:", final_mapping)
end_time = time.time()
final_time = end_time - start_time
makespan = calculate_makespan(final_mapping, etc)

print("Time:", final_time)

order = [10, 14, 0, 11, 4, 8, 6, 2, 12, 15, 8, 12, 5, 7, 5, 7, 10, 6, 11, 10, 3, 0, 11, 0, 11, 6, 8, 7, 11, 5, 6, 13, 2, 8, 14, 6, 15, 9, 12, 12, 13, 0, 11, 15, 3, 13, 12, 8, 2, 12, 9, 14, 2, 14, 2, 7, 1, 11, 13, 14, 1, 5, 1, 5, 4, 5, 11, 14, 2, 10, 10, 10, 15, 8, 12, 6, 6, 6, 4, 2, 8, 4, 9, 6, 4, 12, 14, 10, 2, 5, 6, 10, 14, 7, 2, 12, 5, 2, 2, 6, 6, 3, 7, 5, 7, 14, 11, 4, 6, 10, 6, 12, 8, 13, 1, 0, 3, 8, 7, 13, 9, 14, 14, 7, 6, 0, 6, 1, 6, 14, 12, 3, 5, 4, 11, 8, 12, 12, 13, 7, 0, 15, 11, 9, 3, 12, 5, 3, 2, 15, 11, 6, 9, 13, 10, 1, 1, 14, 3, 9, 6, 14, 15, 3, 2, 2, 3, 4, 7, 6, 4, 5, 4, 11, 11, 1, 3, 10, 12, 6, 9, 0, 10, 1, 9, 15, 13, 11, 11, 1, 8, 4, 3, 5, 11, 10, 10, 4, 5, 7, 7, 8, 12, 15, 8, 9, 10, 9, 14, 1, 11, 8, 0, 14, 10, 8, 7, 0, 7, 8, 14, 10, 9, 9, 15, 0, 14, 3, 11, 10, 4, 14, 15, 12, 7, 8, 8, 9, 10, 4, 2, 14, 1, 8, 14, 14, 12, 6, 2, 8, 1, 10, 5, 14, 10, 12, 11, 9, 6, 6, 4, 13, 4, 11, 11, 10, 13, 15, 11, 6, 1, 1, 10, 9, 9, 9, 11, 10, 6, 7, 12, 5, 6, 15, 15, 15, 4, 7, 6, 15, 4, 3, 1, 5, 2, 9, 11, 2, 11, 2, 11, 13, 6, 15, 9, 10, 9, 9, 7, 12, 14, 13, 9, 12, 11, 4, 2, 8, 3, 2, 0, 12, 7, 0, 5, 2, 12, 13, 15, 15, 15, 13, 13, 9, 6, 2, 3, 12, 9, 6, 11, 14, 3, 15, 2, 12, 5, 15, 13, 11, 1, 9, 7, 7, 12, 15, 8, 3, 0, 12, 11, 14, 13, 10, 12, 7, 7, 7, 7, 7, 15, 7, 10, 11, 12, 15, 11, 6, 13, 2, 11, 3, 0, 9, 0, 15, 13, 0, 7, 15, 9, 6, 6, 9, 12, 1, 8, 15, 3, 1, 0, 12, 10, 3, 11, 11, 2, 9, 3, 6, 4, 12, 5, 8, 0, 0, 1, 14, 9, 9, 10, 6, 14, 2, 1, 9, 2, 3, 3, 3, 3, 3, 11, 10, 15, 14, 11, 9, 3, 6, 14, 3, 15, 11, 14, 3, 13, 7, 3, 6, 7, 1, 6, 6, 11, 5, 11, 11, 15, 14, 6, 3, 3, 1, 5, 8, 0, 11, 15, 6, 5, 3, 7, 0, 2, 2, 3, 4, 1, 1, 4, 7, 14, 12, 11, 8, 11, 14, 3, 8, 7, 8, 15, 12, 11, 6, 10, 11, 15, 10, 9, 8, 12, 6, 1, 11, 10, 15, 10, 1, 3, 9]
makespan = calculate_makespan(order, etc)
print(makespan)
