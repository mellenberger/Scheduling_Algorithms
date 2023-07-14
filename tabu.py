import time
from ETC_Generation import *
from Helper_funcs import *

def generate_neighbors(schedule):
    neighbors = []
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            neighbor = schedule.copy()
            neighbor[i], neighbor[j] = schedule[j], schedule[i] # Swap two tasks
            neighbors.append(neighbor)
    return neighbors

def tabu_search(initial_schedule, etc, tabu_tenure, max_iterations):
    best_schedule = initial_schedule
    best_makespan = calculate_makespan(initial_schedule, etc)

    current_schedule = initial_schedule
    tabu_list = []

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_schedule)
        valid_moves = [schedule for schedule in neighbors if schedule not in tabu_list]

        if not valid_moves:
            break # If there are no valid moves left, stop the search

        current_schedule = min(valid_moves, key=lambda x: calculate_makespan(x, etc))
        current_makespan = calculate_makespan(current_schedule, etc)

        if current_makespan < best_makespan:
            best_schedule = current_schedule
            best_makespan = current_makespan

            tabu_list.append(current_schedule)
            if len(tabu_list) > tabu_tenure:
                tabu_list.pop(0) # Remove the oldest move from the tabu list

    return best_schedule, best_makespan

# Call Tabu to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 5
m = 3
tenure = 20
iterations = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    initial_schedule = initial_mapping(t, m)
    order, makespan = tabu_search(initial_schedule, etc, tenure, iterations)
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
    initial_schedule = initial_mapping(t, m)
    order, makespan = tabu_search(initial_schedule, etc, tenure, iterations)    
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
    initial_schedule = initial_mapping(t, m)
    order, makespan = tabu_search(initial_schedule, etc, tenure, iterations)    
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
    initial_schedule = initial_mapping(t, m)
    order, makespan = tabu_search(initial_schedule, etc, tenure, iterations)    
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