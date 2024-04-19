import random

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

# calculate makespan given a mapping and the ETC
def calculate_makespan(mapping, etc_matrix):
    num_resources = len(etc_matrix[0])
    task_times = [0] * num_resources

    # iterate over each task in the mapping
    for task, resource in enumerate(mapping):
        task_times[resource] += etc_matrix[task][resource]

    # makespan is the maximum time taken by any resource
    return max(task_times)

# generate initial random mapping of tasks to resources
def initial_mapping(num_tasks, num_resources):
    return [random.randint(0, num_resources - 1) for _ in range(num_tasks)]

# generate initial random mapping of tasks to resources
def initial_mapping_deadlines(num_tasks, num_resources, etc, deadlines):
    mapping = [random.randint(0, num_resources - 1) for _ in range(num_tasks)]
    for i in range(num_tasks):
        machine = mapping[i]
        while etc[i][machine] > deadlines[i]:
            machine = random.randint(0, num_resources - 1)
        mapping[i] = machine
    return mapping
