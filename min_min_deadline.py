# import necessary modules
import random
import math
import numpy as np
import time
from ETC_Generation import *
from Helper_funcs import *

def min_min(t, m, etc, deadlines):
    #Initialize Variables
    need_assignment = np.linspace(0, t-1, num=t, dtype=int)
    machine_times = np.zeros(m, dtype=int)
    order = np.zeros(t,  dtype=int)

    while(len(need_assignment) != 0):
        #Calculate times every task would take to run with consideration to machine times
        task_times = machine_times + etc

        #Find task & machine with minimum completion time & assign
        #I = np.argwhere(task_times[need_assignment]==task_times[need_assignment].min())
        #task = I[0][0]
        #machine = I[0][1]
        bestMinInd = [0,0]
        bestMin = float('inf')
        for i in need_assignment:
            for j in range(m):
                val = task_times[i][j]
                if val < bestMin:
                    bestMin = val
                    bestMinInd = [i,j]
        task = bestMinInd[0]
        machine = bestMinInd[1]

        if etc[task][machine] <= deadlines[task]:
            order[task] = machine
        else:
            temp_need_assignment = need_assignment
            temp_task_times = task_times
            while etc[task][machine] > deadlines[task]:
                #Remove assigned task from unmapped list
                ind = np.argwhere(temp_need_assignment==task)
                temp_need_assignment = np.delete(temp_need_assignment, ind)
                #if len(temp_need_assignment) == 0:           
                    #I = np.argwhere(temp_task_times[need_assignment[0]]==temp_task_times[need_assignment[0]].min())
                    #task = I[0][0]
                    #machine = I[0][1]
                bestMinInd = [0,0]
                bestMin = float('inf')
                for i in range(m):
                    val = temp_task_times[need_assignment[0]][i]
                    if val < bestMin:
                        bestMin = val
                        bestMinInd = [need_assignment[0],i]
                task = bestMinInd[0]
                machine = bestMinInd[1]

                if etc[task][machine] > deadlines[task]:
                    temp_task_times[task][machine] = float('inf')

                #else:
                    #bestMinInd = [0,0]
                    #bestMin = float('inf')
                    #for i in temp_need_assignment:
                       # for j in range(m):
                           # val = temp_task_times[i][j]
                           # if val < bestMin:
                            #    bestMin = val
                            #    bestMinInd = [i,j]

                    #task = bestMinInd[0]
                    #machine = bestMinInd[1]
                    #I = np.argwhere(task_times[temp_need_assignment]==task_times[temp_need_assignment].min())
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