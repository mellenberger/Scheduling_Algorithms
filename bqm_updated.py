from dimod import BinaryQuadraticModel
from scipy.stats import gamma
import numpy as np
from dimod import Binary, Real
from dwave.system import DWaveSampler, EmbeddingComposite, AutoEmbeddingComposite
def get_indices(name):
    values = name.split('_')
    task = int(values[0].split('T')[1])
    machine = int(values[1].split('M')[1])
    return [task, machine]
    
## Coeffecient-of-Variation Based (CVB) ETC
# Low task / low machine; high task / low machine; high task / high machine;

t = 15
m = 3
etc = np.zeros((t, m))
q = [0] * t
Bmach = [0] * t

Vtask = 0.1
Vmach = 0.1
utask = 1000
sigma_task = 1/(Vtask**2)
sigma_mach = 1/(Vmach**2)
Btask = utask / sigma_task
for i in range(t):
    q[i] = gamma.rvs(sigma_task, scale=Btask) 
    Bmach[i] = q[i]/sigma_mach
    for j in range(m):        
        etc[i][j] = gamma.rvs(sigma_mach, scale=Bmach[i])


##load etc
etc = np.loadtxt("QUBO_matrices/LT_LM_Inconsistent.txt")

bqm = BinaryQuadraticModel('BINARY')
x = [[(f'T{i}_M{j}') for j in range(m)] for i in range(t+1)]

for i in range(t):
    for j in range(m):
        bqm.add_variable(x[i][j], etc[i][j])
y = 'Y'
bqm.add_variable(y)
for i in range(t):
    c1 = [(x[i][j], 1) for j in range(m)]
    bqm.add_linear_equality_constraint(c1, constant = -1, lagrange_multiplier=20*np.max(np.min(etc)))
for j in range(m):
    c1 = [(x[i][j], -y) for i in range(t)]
    bqm.add_linear_inequality_constraint(c1, constant = 0, lagrange_multiplier=8*np.max(np.min(etc)), label='c2_time_'+str(j))



for j in range(m):
    obj = 0
    for i in range(t):
        obj = etc[i][j] + obj
    for i in range(t):
        bqm.add_variable(x[i][j], obj)  

for i in range(t):
    c1 = [(x[i][j], 1) for j in range(m)]
    bqm.add_linear_equality_constraint(c1, constant = -1, lagrange_multiplier=20*np.max(np.min(etc)))

for j in range(m):
    c1 = [(x[i][j], 1) for i in range(t)]
    bqm.add_linear_inequality_constraint(c1, constant = -1, lagrange_multiplier=8*np.max(np.min(etc)), label='c2_time_'+str(j))
for j in range(m):
    c1 = [(x[i][j], 1) for i in range(t)]
    bqm.add_linear_equality_constraint(c1, constant = -(t/m)-1, lagrange_multiplier=8*np.max(np.min(etc)))





sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=4000)

best = sampleset.first.sample

chosen = []
for i in best:
    if best[i]==1:
        chosen.append(i)
    

machineTimes = np.zeros((m), dtype=float)
for i in range(t):
    index = get_indices(chosen[i])
    machine = index[1]
    task = index[0]
    machineTimes[int(machine)] = machineTimes[int(machine)] + etc[int(task)][int(machine)]

makespan = -np.max(machineTimes)
print(makespan)
print(len(chosen))
