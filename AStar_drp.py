import heapq
import random
import time


MAX_NODES = 1000  # Increase the maximum nodes


class Node:
    def __init__(self, mapping, g_cost, h_cost):
        self.mapping = mapping
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost


def calculate_h(n, max_min_RC, g_cost):
    return max(0, max_min_RC - g_cost)


# Global variable to keep track of the best solution found so far
best_f_cost = float('inf')


def drp_a_star(Ci, si, Sk):
    global best_f_cost  # Declare the global variable
    OPEN = []
    num_tasks = len(Ci)
    num_machines = len(Ci[0])

    initial_mapping = [-1] * num_tasks
    initial_g_cost = 0
    initial_h_cost = 0
    initial_node = Node(initial_mapping, initial_g_cost, initial_h_cost)
    heapq.heappush(OPEN, initial_node)

    iteration = 0

    while OPEN:
        if len(OPEN) > MAX_NODES:
            OPEN = heapq.nsmallest(MAX_NODES, OPEN)

        current_node = heapq.heappop(OPEN)

        # Check if this path is already worse than the best complete path found so far
        if current_node.f_cost > best_f_cost:
            continue

        if all(map(lambda x: x != -1, current_node.mapping)):
            best_f_cost = min(best_f_cost, current_node.f_cost)
            return current_node.mapping

        for task in range(num_tasks):
            for machine in range(num_machines):
                if current_node.mapping[task] != -1:
                    continue

                new_mapping = current_node.mapping.copy()
                new_mapping[task] = machine

                new_g_cost = current_node.g_cost + Ci[task][machine]

                unassigned_tasks = [i for i in range(num_tasks) if new_mapping[i] == -1]
                if unassigned_tasks:
                    max_min_RC = min([min(Ci[i]) for i in unassigned_tasks])
                    new_h_cost = calculate_h(new_mapping, max_min_RC, new_g_cost)
                else:
                    new_h_cost = 0  # or some other default value

                # Prune node if its f_cost is already greater than the best f_cost found so far
                if new_g_cost + new_h_cost > best_f_cost:
                    continue

                new_node = Node(new_mapping, new_g_cost, new_h_cost)
                heapq.heappush(OPEN, new_node)

        iteration += 1
        if iteration % 100 == 0:
            print(f"Iteration {iteration}, OPEN size: {len(OPEN)}")


Ci = [[random.randint(50, 150) for _ in range(16)] for _ in range(64)]
si = [1 for _ in range(32)]
Sk = [100 for _ in range(16)]
best_f_cost = float('inf')
start_time = time.time()
final_mapping = drp_a_star(Ci, si, Sk)
print("Final mapping:", final_mapping)
end_time = time.time()
final_time = end_time - start_time
print(final_time)