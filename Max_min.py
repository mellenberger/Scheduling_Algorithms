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

def max_min(t, m, etc):
    #Initialize Variables
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    machine_times = np.zeros(m, dtype=int) 
    minimum_times = np.min(etc, axis=1)
    order = np.zeros(t,  dtype=int)

    for i in range(t):
        #Calculate times every task would take to run with consideration to machine times
        task_times = machine_times + etc

        #Find minimum completion time for each task
        minimum_times = np.min(task_times, axis=1)

        #Chose maximum time from minimum times to assign
        assign_max = np.argwhere(minimum_times==minimum_times[need_assignment].max())

        #Find index for task & machine for chosen assignment & assign
        index = np.argwhere(task_times==minimum_times[assign_max])
        task = index[0][0]
        machine = index[0][1]
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