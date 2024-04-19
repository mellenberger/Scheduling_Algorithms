import networkx as nx
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite
from dwave.system import LeapHybridSampler
from scipy.stats import gamma
import numpy as np
import dwave.inspector
import dimod
from Helper_funcs import *


G = nx.Graph()

## Coeffecient-of-Variation Based (CVB) ETC
# Low task / low machine; high task / low machine; high task / high machine;
t = 10
m = 9
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



G = nx.Graph()
etc = np.loadtxt("QUBO_matrices\HT_HM_Consistent.txt")
t = 15
m = 3
for i in range(t*m):
    for j in range(t*m):
        if i // m != j // m: 
            G.add_edge(i,j)

Q = defaultdict(float)
other = True
# Constraint
#lagrange=(np.average(etc)+np.amax(etc))/2
# lagrange1 = 10*np.min(etc)
# lagrange2 = 10*np.max(etc)-(np.min(etc)/3)
# lagrange3 =20
lagrange1=13
lagrange2=-2
lagrange3=1
for i in range(t*m):
    Q[(i,i)] += -(1)*lagrange1
    for j in range(i+1,t*m):
        #Q[(i,j)] += 2*lagrange 
        if i // m == j // m: 
            row_i, col_i = divmod(i, m)
            row_j, col_j = divmod(j, m)
            print(i,j)
            Q[(i,j)] += ((2)*lagrange1)+2*(etc[row_i][col_i]*etc[row_j][col_j])*lagrange3


for i in range(t*m):
    row_i, col_i = divmod(i, m)
    print(row_i,col_i)
    Q[(i,t*m)] = -2*etc[row_i][col_i]*lagrange3


Q[(t*m, t*m)] = 1+m*lagrange2 +m*lagrange3

# Objective
for i in range(t * m):
    row = i // m
    col = i % m
    Q[(i,i)] += (int(etc[row][col])^2)*lagrange3 - (etc[row][col])*lagrange2

t=15
m=3
etc = np.loadtxt("QUBO_matrices/LT_LM_Inconsistent.txt")
for i in range(t):
    for j in range(m):
        etc[i][j] = etc[i][j]/100
etc = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

etc = [
    [15,2],
    [3,30]
]

etc = [
    [15,2],
    [30,3],
    [10,15]
]
sampler = EmbeddingComposite(DWaveSampler(token='DEV-e4731ecb7eaebd776461629eedd8fd2df50f19df'))
#sampleset = sampler.sample_qubo(Q, num_reads=100, chain_strength=100)
#print(sampleset)

for i in range(1,25):
    bqm = dimod.BinaryQuadraticModel.from_qubo(Q)
    sampleset = sampler.sample(bqm, num_reads=100)
    #dwave.inspector.show(sampleset)
    best = sampleset.first.sample
    chosen = []
    order = [-1]*t
    for i in best:
        if best[i]==1 and i != t*m:
            chosen.append(i)
            row_index, col_index = divmod(i, m)
            # row_index = i // m
            # col_index = i % m
            order[row_index] = col_index
    print("chose: ", len(chosen))
    makespan = calculate_makespan(order,etc)
    print("makespan: ", makespan)



