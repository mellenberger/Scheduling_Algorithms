import random
import numpy as np
from ETC_deadlines import CVB_ETC_1  # or CVB_ETC_2, depending on your needs

# GA parameters
populationSize = 100
numGenerations = 100
mutationRate = 0.01
tournamentSize = 5
deadline_penalty = 1000  # Penalty for missing a deadline

# Task and machine parameters
numTasks = 256
numMachines = 32
vtask = 1.0  # Variance for tasks (example value)
vmach = 1.0  # Variance for machines (example value)
utask = 1000  # Mean task time (example value)
consistency = 'consistent'  # 'consistent', 'partiallyconsistent', or 'inconsistent'

# Generate ETC matrix and deadlines
CVB_ETC_1(numTasks, numMachines, vtask, vmach, utask, 'etc.txt', consistency)

with open('etc.txt', 'r') as file:
    lines = file.readlines()
    etcMatrix = [list(map(float, line.split()[:-1])) for line in lines]
    deadlines = [float(line.split()[-1]) for line in lines]


# Initialize population
population = np.random.randint(0, numMachines, size=(populationSize, numTasks))


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
            print("MISS", i)
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
    for i in range(populationSize):
        for j in range(numTasks):
            if random.random() < mutationRate:
                newPopulation[i, j] = np.random.randint(0, numMachines)
    population = newPopulation
    for i in range(populationSize):
        fitness[i] = fitness_function(population[i])
    best_index_in_gen = np.argmax(fitness)
    if fitness[best_index_in_gen] > best_fitness:
        best_fitness = fitness[best_index_in_gen]
        best_solution = population[best_index_in_gen]

# Show results
print(f"Best mapping: {best_solution}")
print(f"Best makespan: {-best_fitness}")

fitness_function(population[best_index_in_gen])
