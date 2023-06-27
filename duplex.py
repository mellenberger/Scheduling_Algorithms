# import necessary modules
import random
import math
import numpy as np
from ETC_Generation import *
from Helper_funcs import *
from Min_Min import *
from Max_min import *

#Create ETC
t = 5
m = 3
etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)

#Run both min-min & max-min to obtain results
minmin_result, Minmin_makespan = min_min(t, m, etc)
maxmin_result, Maxmin_makespan = max_min(t, m, etc)

#Determine & keep better result
if Minmin_makespan < Maxmin_makespan:
    result = minmin_result
    makespan = Minmin_makespan
else:
    result = maxmin_result
    makespan = Maxmin_makespan

print("Order:", result)
print("Makespan:", makespan)

