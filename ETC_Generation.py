from scipy.stats import gamma
import numpy as np
import random

def CVB_ETC_1(t, m, Vtask, Vmach, utask):
    ## Coeffecient-of-Variation Based (CVB) ETC
    # Low task / low machine; high task / low machine; high task / high machine;
    etc_matrix = np.zeros((t, m))
    q = [0] * t
    Bmach = [0] * t

    sigma_task = 1/(Vtask**2)
    sigma_mach = 1/(Vmach**2)
    Btask = utask / sigma_task
    for i in range(t):
        q[i] = gamma.rvs(sigma_task, scale=Btask) 
        Bmach[i] = q[i]/sigma_mach
        for j in range(m):        
            etc_matrix[i][j] = gamma.rvs(sigma_mach, scale=Bmach[i])
    return etc_matrix

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

def RB_ETC_1(t,m,Rtask,Rmach):
    # Range based ETC Matrix
    tau = [0] * t
    e = [[0 for x in range(m)] for y in range(t)]
    for i in range(t):
        tau[i]=random.randrange(1,Rtask)
        for j in range(m):
            e[i][j] = tau[i] * random.randrange(1,Rmach)
    return e