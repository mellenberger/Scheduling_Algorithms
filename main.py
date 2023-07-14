from Min_Min import *
from Max_min import *

#Keeping these calls in a separate file due to Duplex relying on min-min and max-min algorithms

#Create ETC Parameters
t = 3200
m = 100

#Low task / Low machine heterogeneity
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = min_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("Low task, Low machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / high machine
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.6, 0.6, 1000)
    start_time = time.time()
    order, makespan = min_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("High Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / low machine
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.5, 0.1, 1000)
    start_time = time.time()
    order, makespan = min_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("High Task, Low Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# low task / high machine
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_2(t, m, 0.1, 0.6, 1000)
    start_time = time.time()
    order, makespan = min_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("Low Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)

# Call Max-Min to run 100 times, gather average makespan & time
#Low task / Low machine heterogeneity
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = max_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("Low task, Low machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / high machine
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.6, 0.6, 1000)
    start_time = time.time()
    order, makespan = max_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("High Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / low machine
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.5, 0.1, 1000)
    start_time = time.time()
    order, makespan = max_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("High Task, Low Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# low task / high machine
average_time = 0
average_makespan = 0
for i in range(25):
    etc = CVB_ETC_2(t, m, 0.1, 0.6, 1000)
    start_time = time.time()
    order, makespan = max_min(t,m,etc)
    end_time = time.time()
    time_lapsed = end_time - start_time
    average_time += time_lapsed
    average_makespan += (makespan)
    time_convert(time_lapsed)

average_time = average_time/25
average_makespan = average_makespan/25

print("Low Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)