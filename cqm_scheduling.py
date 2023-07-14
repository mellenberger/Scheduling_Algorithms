from dimod import ConstrainedQuadraticModel
from dimod import Binary, Real
from dwave.system import LeapHybridCQMSampler
from scipy.stats import gamma
import numpy as np
import random

def get_indices(name):
    values = name.split('_')
    task = int(values[0].split('T')[1])
    machine = int(values[1].split('M')[1])
    return [task, machine]

def CVB_ETC_2(t,m,vtask,vmach, umach):
    # Coefficient of Variation ETC matrix
    # Low task heterogeneity high machine heterogeneity
    atask = 1 / (vtask**2)
    amach = 1 / (vmach**2)
    bmach = umach / amach
    p = []
    btask = []
    e = [[0 for x in range(m)] for y in range(t)]
    for j in range (m):
        p.append(random.gammavariate(amach,bmach))
        btask.append(p[j] / atask)
        for i in range (t):
            e[i][j] = random.gammavariate(atask,btask[j])
    return e

tasks = 512
machines = 16
etc = CVB_ETC_2(tasks, machines, 0.1, 0.6, 1000)
## Coeffecient-of-Variation Based (CVB) ETC
# Low task / low machine; high task / low machine; high task / high machine;

tasks = 512
machines = 16
etc = np.zeros((tasks, machines))
q = [0] * tasks
Bmach = [0] * tasks

Vtask = 0.5
Vmach = 0.1
utask = 1000
sigma_task = 1/(Vtask**2)
sigma_mach = 1/(Vmach**2)
Btask = utask / sigma_task
for i in range(tasks):
    q[i] = gamma.rvs(sigma_task, scale=Btask) 
    Bmach[i] = q[i]/sigma_mach
    for j in range(machines):        
        etc[i][j] = gamma.rvs(sigma_mach, scale=Bmach[i])

np.savetxt('etc_LH_1.txt', etc)

y = [Real(f'runtime_{j}') for j in range((machines))]
x = [[Binary(f'T{i}_M{j}') for j in range((machines))]
     for i in range(len(etc))]

makespan = [0] * machines
for j in range(machines):
    for i in range(tasks):
        makespan[j] += etc[i][j] * x[i][j]

cqm = ConstrainedQuadraticModel()
# minimizing max
t = Real(f'objf')
objf = t
for i in range(machines):
    cqm.add_constraint(y[i] - t <= 0, label=f'min_max_{i}')

# y = makespan for each machine
for i in range(machines):
    cqm.add_constraint(y[i]-makespan[i] == 0, label=f'runtime_machine_{i}')


cqm.set_objective(objf)

#Must assign task to only 1 machine
for i in range((tasks)):
    cqm.add_constraint(sum(x[i]) == 1, label=f'task_placing_{i}')

print(cqm)

sampler = LeapHybridCQMSampler()     

sampleset = sampler.sample_cqm(cqm, time_limit = 20, label="Scheduling-LH1")  
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  
if len(feasible_sampleset):      
   best = feasible_sampleset.first
   print("{} feasible solutions of {}.".format(
      len(feasible_sampleset), len(sampleset)))

scheduled_task = [key for key, val in best.sample.items() if 'T' in key and val]   
print("{} tasks are scheduled.".format(len(scheduled_task)))     
makespans = {key: val for key, val in best.sample.items() if 'runtime' in key and val}
print("Makespan:", makespans[max(makespans)])
