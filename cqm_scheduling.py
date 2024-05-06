#Steps to run:
# 1. Import all necessary libraries 
# 2. Define get_indices function 
# 3. Initialize task & machine variables 
# 4. Load ETC from either standard file (4a) or deadline file (4b)
# 5. Initialize problem variables, x, y, makespan, and taskTimes 
# 6. Initalize CQM 
# 7. Set up constraint 1 
# 8. Set up constraint 2
# 9. Set objective function
# 10. Set up constraint 3
# 11. Set up constaint 4 (Only for deadline problem, do not add for standard)
# 12. Print CQM for viewing
# 13. Initialize solver (token may be needed here)
# 14. Sample CQM
# 15. Filter results
# 16. Print number of scheduled tasks
# 17. Print final makespan for best solution
# 18. Check for missed deadlines if needed

# (1) import statements
from dimod import ConstrainedQuadraticModel
from dimod import Binary, Real
from dwave.system import LeapHybridCQMSampler
import numpy as np

# (2) function to get scheduled task and machine pairs from solution set
def get_indices(name):
    values = name.split('_')
    task = int(values[0].split('T')[1])
    machine = int(values[1].split('M')[1])
    return [task, machine]

# (3) initialize task & machines variables
tasks = 15
machines = 3

# (4a) load standard ETC no deadlines
etc = np.loadtxt("LT_LM_Inconsistent.txt")

# (4b) Load with deadlines
with open('largerDeadline_matrices/HT_HM_PartiallyConsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]


# (5) Initialize problem variables
y = [Real(f'runtime_{j}') for j in range((machines))]
x = [[Binary(f'T{i}_M{j}') for j in range((machines))]
     for i in range(len(etc))]

makespan = [0] * machines
for j in range(machines):
    for i in range(tasks):
        makespan[j] += etc[i][j] * x[i][j]

taskTimes = [0] * tasks
for j in range(machines):
    for i in range(tasks):
        taskTimes[i] += etc[i][j] * x[i][j]

# (6) Initialize CQM model
cqm = ConstrainedQuadraticModel()

# (7) minimizing max
t = Real(f'objf')
objf = t
for i in range(machines):
    cqm.add_constraint(y[i] - t <= 0, label=f'min_max_{i}')

# (8) y = makespan for each machine
for i in range(machines):
    cqm.add_constraint(y[i]-makespan[i] == 0, label=f'runtime_machine_{i}')

# (9) Set objective function
cqm.set_objective(objf)

# (10) Must assign task to only 1 machine
for i in range((tasks)):
    cqm.add_constraint(sum(x[i]) == 1, label=f'task_placing_{i}')

# (11) Must adhere to deadline
for i in range((tasks)):
    cqm.add_constraint(taskTimes[i] <= deadlines[i], label=f'task_deadline_{i}')

# (12) View CQM to ensure problem is set correctly
print(cqm)

# (13) Initialize hybrid sampler
sampler = LeapHybridCQMSampler()     

# (14) Sample CQM
sampleset = sampler.sample_cqm(cqm, time_limit = 5, label="LT_LM_Inconsistent")  

# (15) Filter results to show only feasible solutions
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  
if len(feasible_sampleset):      
   best = feasible_sampleset.first
   print("{} feasible solutions of {}.".format(
      len(feasible_sampleset), len(sampleset)))

# (16) Ensure all tasks are scheduled (All feasible results should have all tasks scheduled)
scheduled_task = [key for key, val in best.sample.items() if 'T' in key and val]   
print("{} tasks are scheduled.".format(len(scheduled_task)))   

# (17) Print makespan of best result
makespans = [val for key, val in best.sample.items() if 'runtime' in key and val]
print("Makespan:", max(makespans))

# (18) Use this to check for missed deadlines
for i in range(len(scheduled_task)):
    task, machine = get_indices(scheduled_task[i])
    if etc[task][machine] > deadlines[task]:
        print("MISS", task)