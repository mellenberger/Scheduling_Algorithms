from scipy.stats import gamma
import numpy as np

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