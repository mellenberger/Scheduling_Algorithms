import random
import numpy as np
from ETC_deadlines import CVB_ETC_1  # or CVB_ETC_2, depending on your needs
from Helper_funcs import *
import time


def GA_deadline(etcMatrix,deadlines,numTasks,numMachines):
    # GA parameters
    populationSize = 100
    numGenerations = 1500
    mutationRate = 0.01
    tournamentSize = 5
    deadline_penalty = 10000  # Penalty for missing a deadline

    # Initialize population
    #population = np.random.randint(0, numMachines, size=(populationSize, numTasks))
    population = np.zeros((populationSize, numTasks), dtype=int)
    for i in range(populationSize):
        population[i] = initial_mapping_deadlines(numTasks, numMachines,etcMatrix,deadlines)

    # Define the fitness function
    def fitness_function(chromosome):
        machineTimes = np.zeros(numMachines)
        missed_deadlines = 0
        for i in range(numTasks):
            machine = chromosome[i]
            task = i
            machineTimes[machine] += etcMatrix[task][machine]
            if etcMatrix[task][machine] > deadlines[i]:
                missed_deadlines += 1
        return -np.max(machineTimes) - missed_deadlines * deadline_penalty


    fitness = np.zeros(populationSize)

    # Calculate initial fitness
    for i in range(populationSize):
        fitness[i] = fitness_function(population[i])

    best_solution = None
    best_fitness = float('-inf')

    for gen in range(numGenerations):
        newPopulation = np.zeros((populationSize, numTasks), dtype=int)
        for i in range(0, populationSize, 2):
            if i == populationSize - 1:
                newPopulation[i] = population[i]
                break
            tournament1 = np.random.choice(populationSize, tournamentSize)
            tournament2 = np.random.choice(populationSize, tournamentSize)
            parent1 = population[tournament1[np.argmax(fitness[tournament1])]]
            parent2 = population[tournament2[np.argmax(fitness[tournament2])]]
            crossoverPoint = np.random.randint(1, numTasks)
            newPopulation[i] = np.concatenate((parent1[:crossoverPoint], parent2[crossoverPoint:]))
            newPopulation[i + 1] = np.concatenate((parent2[:crossoverPoint], parent1[crossoverPoint:]))
        # Mutation
        for i in range(populationSize):
            for j in range(numTasks):
                if random.random() < mutationRate:
                    new_resource = random.randint(0,numMachines-1)
                    while etc[j][new_resource] > deadlines[j]:
                        new_resource = random.randint(0,numMachines-1)
                    newPopulation[i][j] = new_resource
        population = newPopulation
        for i in range(populationSize):
            fitness[i] = fitness_function(population[i])
        best_index_in_gen = np.argmax(fitness)
        if fitness[best_index_in_gen] > best_fitness:
            best_fitness = fitness[best_index_in_gen]
            best_solution = population[best_index_in_gen]

    # Show results
    best_makespan = calculate_makespan(best_solution,etcMatrix)
    return best_solution, best_makespan


# Task and machine parameters
numTasks = 1000
numMachines = 32
average_time = 0
t = numTasks

# Call GA for each ETC, gather average makespan & time

# High task / Low machine heterogeneity / Inconsistent
with open('largerDeadline_matrices/HT_LM_Inconsistent.txt', 'r') as file:
    lines = file.readlines()
    etc = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]

start_time = time.time()
order, makespan = GA_deadline(etc,deadlines,numTasks,numMachines)
end_time = time.time()
average_time += (end_time - start_time)
print("High task, Low machine, Inconsistent:")
print("Makespan:", makespan)

count = 0
for i in range(t):
    machine = order[i]
    if etc[i][machine] > deadlines[i]:
        print("MISS",i)
        count += 1
print("Missed:",count)


average_time = average_time / 12
print("Average Time:", average_time)