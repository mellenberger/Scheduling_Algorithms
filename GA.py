import random
import numpy as np
from ETC_Generation import *
from Helper_funcs import *
import time


def GA(numTasks, numMachines, etcMatrix):

    # Genetic Algorithm parameters
    populationSize = 100
    numGenerations = 200
    mutationRate = 0.01
    tournamentSize = 5
    population = np.zeros((populationSize, numTasks), dtype=int)

    # Initialize population
    for i in range(populationSize):
        population[i] = [random.randint(0, numMachines-1) for _ in range(numTasks)]

    # Define the fitness function
    def fitness_function(chromosome, numTasks, numMachines, etcMatrix):
        machineTimes = np.zeros((numMachines), dtype=int)
        for i in range(numTasks):
            machine = chromosome[i]
            task = i
            machineTimes[int(machine)] = machineTimes[int(machine)] + etcMatrix[int(task)][int(machine)]
        fitness = -np.max(machineTimes)
        return fitness

    for gen in range(numGenerations):
        # Calculate fitness
        fitness = np.zeros(populationSize, dtype=int)
        for i in range(populationSize):
            fitness[i] = fitness_function(population[i], numTasks, numMachines, etcMatrix)

        # Tournament selection
        newPopulation = np.zeros((populationSize, numTasks), dtype=int)
        for i in range(populationSize):
            tournament = random.sample(range(1, populationSize), tournamentSize)
            best = np.argmax(fitness[tournament])
            newPopulation[i] = population[tournament[best]]

        # Single-point crossover
        for i in range(0,2, populationSize):
            if i == populationSize: # If we have an odd population size
                break
            crossoverPoint = random.randint(1,numTasks)
            parent1 = newPopulation[i]
            parent2 = newPopulation[i+1]
            newPopulation[i] = np.concatenate((parent1[0:crossoverPoint+1], parent2[crossoverPoint+1:numTasks]))
            newPopulation[i+1] = np.concatenate((parent2[0:crossoverPoint+1], parent1[crossoverPoint+1:numTasks]))
        
        # Mutation
        for i in range(populationSize):
            for j in range(numTasks):
                if random.random() < mutationRate:
                    newPopulation[i,j] = random.randint(0,numMachines-1)
        
        # Replace the old population with the new one
        population = newPopulation

    for i in range(populationSize):
        fitness[i] = fitness_function(population[i], numTasks, numMachines, etcMatrix)
    best = np.argmax(fitness[tournament])
    makespan = - np.max(fitness[tournament])
    result = population[best]

    return result, makespan

# Call GA to run 100 times, gather average makespan & time
# Low task / Low machine heterogeneity
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.1, 0.1, 1000)
    start_time = time.time()
    order, makespan = GA(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("Low task, Low machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / high machine
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.6, 0.6, 1000)
    start_time = time.time()
    order, makespan = GA(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("High Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# high task / low machine
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_1(t, m, 0.5, 0.1, 1000)
    start_time = time.time()
    order, makespan = GA(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("High Task, Low Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)


# Low task heterogeneity high machine
t = 3200
m = 100
average_makespan = 0
average_time = 0
for i in range(25):
    etc = CVB_ETC_2(t, m, 0.1, 0.6, 1000)
    start_time = time.time()
    order, makespan = GA(t,m,etc)
    end_time = time.time()
    average_makespan = average_makespan + makespan
    time_lapsed = end_time - start_time
    average_time = average_time + time_lapsed
    time_convert(time_lapsed)

average_makespan = average_makespan / 25
average_time = average_time / 25
print("Low Task, High Machine:")
print("Average Time:", average_time)
print("Average Makespan:", average_makespan)