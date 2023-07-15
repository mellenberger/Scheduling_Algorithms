import random

import numpy as np

import time




def calculate_makespan(schedule, etc):

    machines = [0]*len(etc[0])  # Initialize the time of each machine to 0

    for task in schedule:

        machine = np.argmin(machines)  # Find the machine with the shortest time

        machines[machine] += etc[task][machine]  # Assign the task to this machine

    return max(machines)  # The makespan is the maximum time




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




# Example usage:




num_tasks = 512

num_machines = 16

etc = [[random.randint(1, 10) for _ in range(num_machines)] for _ in range(num_tasks)]  # Random 2D ETC matrix




initial_schedule = list(range(num_tasks))  # Initial schedule is just the tasks in order

random.shuffle(initial_schedule)  # Shuffle the initial schedule




max_iterations = 100

num_neighbors = 50  # Number of neighbors to generate in each iteration




start_time = time.time()

best_schedule, best_makespan = tabu_search(initial_schedule, etc, max_iterations, num_neighbors)

end_time = time.time()




print('Best Schedule:', best_schedule)

print('Best Makespan:', best_makespan)

print('Runtime:', end_time - start_time, 'seconds')