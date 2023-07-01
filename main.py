from Min_Min import *
from Max_min import *

#Keeping these calls in a separate file due to Duplex relying on min-min and max-min algorithms

#High task heterogeneity low machine heterogeneity
#Create ETC
t = 3200
m = 100
average_time = 0
average_makespan = 0

for i in range(100):
    etc = CVB_ETC_1(t, m, 0.3, 0.1, 1000)
    start_time = time.time()
    order, makespan = min_min(t,m,etc)
    end_time = time.time()
    average_time += (end_time - start_time)
    average_makespan += (makespan)

average_time = average_time/100
average_makespan = average_makespan/100

print("Average Time:", average_time)
print("Average Makespan:", average_makespan)

# Call Max-Min to run 100 times, gather average makespan & time
#High task heterogeneity low machine heterogeneity
t = 3200
m = 100
average_time = 0
average_makespan = 0

for i in range(100):
    etc = CVB_ETC_1(t, m, 0.3, 0.1, 1000)
    start_time = time.time()
    order, makespan = max_min(t,m,etc)
    end_time = time.time()
    average_time += (end_time - start_time)
    average_makespan += (makespan)

average_time = average_time/100
average_makespan = average_makespan/100

print("Average Time:", average_time)
print("Average Makespan:", average_makespan)