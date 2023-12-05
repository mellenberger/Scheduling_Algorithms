import numpy as np
import random

def add_deadlines(t,m,o_file_name,n_file_name):
    e = np.loadtxt(o_file_name)

    # Add deadlines for each task
    d = np.zeros((t,1))
    for i in range(t):
        d[i] = random.uniform(min(e[i]), max(e[i]))
    e = np.hstack((e,d))

    file1 = open(n_file_name,'w')
    for i in range(t):
        print(*e[i], file = file1)

t=512
m=16
add_deadlines(t, m, "LT_LM_Consistent.txt", "deadline_matrices/LT_LM_Consistent.txt")
add_deadlines(t, m, "LT_LM_PartiallyConsistent.txt", "deadline_matrices/LT_LM_PartiallyConsistent.txt")

add_deadlines(t, m, "LT_HM_Inconsistent.txt", "deadline_matrices/LT_HM_Inconsistent.txt")
add_deadlines(t, m, "LT_HM_Consistent.txt", "deadline_matrices/LT_HM_Consistent.txt")
add_deadlines(t, m, "LT_HM_PartiallyConsistent.txt", "deadline_matrices/LT_HM_PartiallyConsistent.txt")

add_deadlines(t, m, "HT_LM_Inconsistent.txt", "deadline_matrices/HT_LM_Inconsistent.txt")
add_deadlines(t, m, "HT_LM_Consistent.txt", "deadline_matrices/HT_LM_Consistent.txt")
add_deadlines(t, m, "HT_LM_PartiallyConsistent.txt", "deadline_matrices/HT_LM_PartiallyConsistent.txt")

add_deadlines(t, m, "HT_HM_Inconsistent.txt", "deadline_matrices/HT_HM_Inconsistent.txt")
add_deadlines(t, m, "HT_HM_Consistent.txt", "deadline_matrices/HT_HM_Consistent.txt")
add_deadlines(t, m, "HT_HM_PartiallyConsistent.txt", "deadline_matrices/HT_HM_PartiallyConsistent.txt")
