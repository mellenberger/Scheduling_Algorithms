# import necessary modules
import random
import math
import numpy as np
from ETC_Generation import *
from Helper_funcs import *

def max_min(t, m, etc, deadlines):
    #Initialize Variables
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    machine_times = np.zeros(m, dtype=int) 
    minimum_times = np.min(etc, axis=1)
    order = np.zeros(t,  dtype=int)

    while(len(need_assignment) != 0):
        #Calculate times every task would take to run with consideration to machine times
        task_times = machine_times + etc

        #Find minimum completion time for each task
        minimum_times = np.min(task_times, axis=1)

        #Chose maximum time from minimum times to assign
        #assign_max = np.argwhere(minimum_times==minimum_times[need_assignment].max())

        #Find index for task & machine for chosen assignment & assign
        #index = np.argwhere(task_times==minimum_times[assign_max])

        bestMax = 0
        for i in need_assignment:
                val = minimum_times[i]
                if val > bestMax:
                    bestMax = val
                    task = i
        machine = np.argmin(task_times[task])

        #task = index[0][0]
       # machine = index[0][1]
        if etc[task][machine] <= deadlines[task]:
            order[task] = machine
        else:
            temp_need_assignment = need_assignment
            temp_minimum_times = minimum_times
            temp_task_times = task_times
            while etc[task][machine] > deadlines[task]:
                #Remove assigned task from unmapped list
                ind = np.argwhere(temp_need_assignment==task)
                temp_need_assignment = np.delete(temp_need_assignment, ind)
                #if len(temp_need_assignment) == 0:
                bestMax = 0
                for i in temp_need_assignment:
                        val = temp_minimum_times[i]
                        if val > bestMax:
                            bestMax = val
                            task = i
                machine = np.argmin(task_times[task])
                #assign_max = np.argwhere(temp_minimum_times==temp_minimum_times[need_assignment].max())
                #I = np.argwhere(task_times==temp_minimum_times[assign_max])
                #task = I[0][0]
                #machine = I[0][1]
                if etc[task][machine] > deadlines[task]:
                    temp_task_times[task][machine] = float('inf')
                    temp_minimum_times = np.min(temp_task_times, axis=1)
               # else:
                    #assign_max = np.argwhere(minimum_times==minimum_times[temp_need_assignment].max())
                    #I = np.argwhere(task_times==minimum_times[assign_max])

                    #task = I[0][0]
                    #machine = I[0][1]
                
            order[task] = machine
        #Remove assigned task from unmapped list
        ind = np.argwhere(need_assignment==task)
        need_assignment = np.delete(need_assignment, ind)
        #Update machine times
        machine_times[machine] = machine_times[machine] + etc[task][machine]

    makespan = calculate_makespan(order, etc)

    return order, makespan