# import necessary modules
import random
import math
import numpy as np
from ETC_Generation import *
from Helper_funcs import *

#Create ETC
t = 5
m = 3
etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)

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
    print(order)

    makespan = calculate_makespan(order, etc)
    print("Makespan:", makespan)

    return order, makespan