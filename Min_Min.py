# import necessary modules
import random
import math
import numpy as np
from ETC_Generation import *
from Helper_funcs import *

def min_min(t, m, etc):
    #Initialize Variables
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    machine_times = np.zeros(m, dtype=int)
    order = np.zeros(t,  dtype=int)

    for i in range(t):
        #Calculate times every task would take to run with consideration to machine times
        task_times = machine_times + etc

        #Find task & machine with minimum completion time & assign
        I = np.argwhere(task_times==task_times[need_assignment].min())
        task = I[0][0]
        machine = I[0][1]
        order[task] = machine

        #Remove assigned task from unmapped list
        ind = np.argwhere(need_assignment==task)
        need_assignment = np.delete(need_assignment, ind)

        #Update machine times
        machine_times[machine] = machine_times[machine] + etc[task][machine]

    makespan = calculate_makespan(order, etc)

    return order, makespan