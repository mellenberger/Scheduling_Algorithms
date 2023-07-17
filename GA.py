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


# Call GA for each ETC, gather average time & each makespan
t = 512
m = 16
average_time = 0

# Low task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / Low machine heterogeneity / Consistent
etc = np.loadtxt("LT_LM_Consistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, Low machine, Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("LT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Inconsistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("LT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# Low task / High machine heterogeneity / Consistent
etc = np.loadtxt("LT_HM_Consistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("Low task, High machine, Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_LM_Inconsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_LM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / Low machine heterogeneity / Consistent
etc = np.loadtxt("HT_LM_Consistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Inconsistent
etc = np.loadtxt("HT_HM_Inconsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Inconsistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Partially Consistent
etc = np.loadtxt("HT_HM_PartiallyConsistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Partially Consistent:")
print("Makespan:", makespan)

# High task / High machine heterogeneity / Consistent
etc = np.loadtxt("HT_HM_Consistent.txt")
start_time = time.time()
order, makespan = GA(t, m, etc)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, High machine, Consistent:")
print("Makespan:", makespan)

average_time = average_time / 12
print("Average Time:", average_time)