# import necessary modules
import random
import math
import numpy as np
from ETC_Generation import *
from Helper_funcs import *

#Call Function to create ETC
t = 5
m = 3
etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)

#Initialize Variables
need_assignment = np.linspace(0, t-1, num=t, dtype=int)
machine_times = np.zeros(m, dtype=int)
order = np.zeros(t,  dtype=int)

for i in range(t):
    #Choose arbitrary task to assign
    assign = np.random.choice(need_assignment)

    #Find machine that will be avaible soonest & assign task to that machine
    I = np.argmin(machine_times)
    order[assign] = I

    #Remove assigned task from unmapped task list
    ind = np.argwhere(need_assignment==assign)
    need_assignment = np.delete(need_assignment, ind)

    #Update machine time availability
    machine_times[I] = machine_times[I] + etc[assign][I]
print("Mapping:",order)

makespan = calculate_makespan(order, etc)
print("Makespan:", makespan)