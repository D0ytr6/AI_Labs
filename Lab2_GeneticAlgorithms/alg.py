import math
import os
import random

POPULATION_SIZE = 8
ONE_INDIVIDUAL_SIZE = 8
MAX_GENERATION = 50
pt_crossover = 0.61
pm_mutation = 0.01

best = 0
fit_value = []

# fitness score calculation ............
def fitness_score():
    global populations, best
    global fit_value
    fit_score = []
    for i in range(POPULATION_SIZE):
        chromosome_value = 0
        for j in range(ONE_INDIVIDUAL_SIZE - 1, -1, -1):
            chromosome_value += populations[i][j] * (2 ** (7 - j))
        print(f'chromosome_value in 10 system = {chromosome_value}')
        func_result = - (math.pow((chromosome_value - 1), 2) / 256)
        print(f'func res = {func_result}')
        fit_value.append(func_result)

    # sorting to grow
    # fit_value, populations = zip(*sorted(zip(fit_value, populations), reverse=True))
    populations = list(populations)
    # best = fit_value[0]
    # print(type(populations))
    print(f'fit_value {fit_value}')
    print(f'population {populations}')
    print(f'best value {best}')

def selectparent():
    global parents, fit_value, populations
    total_sum = sum(fit_value)
    print(f'sum {total_sum}')
    # find normalized form and create a list
    normalized_fitness_form = [i / total_sum for i in fit_value]

    # find cumulative fitness values for roulette wheel selection
    cumulative_fitness_value = []
    start = 0
    for norm_value in normalized_fitness_form:
        start = start + norm_value
        cumulative_fitness_value.append(start)

    print(f'normalized {normalized_fitness_form}')
    print(f'cumulative {cumulative_fitness_value}')

    for count in range(POPULATION_SIZE):
        rand_numb = random.uniform(0, 1)
        for score in cumulative_fitness_value:
            if rand_numb <= score:
                parents.append(populations[count])
                break

    print(f'parents {parents}')
    for i in range(POPULATION_SIZE):
        chromosome_value = 0
        for j in range(ONE_INDIVIDUAL_SIZE - 1, -1, -1):
            chromosome_value += parents[i][j] * (2 ** (7 - j))
        print(f'chromosome_value in 10 system = {chromosome_value}')


def crossover2():
    global parents, fit_value




def crossover():
    global parents
    print(parents)
    cross_point = random.randint(0, ONE_INDIVIDUAL_SIZE - 1)
    print(cross_point)
    rand_1 = random.randint(0, 7)
    rand_2 = random.randint(0, 7)
    fst_parent_bit = parents[rand_1][cross_point:]
    sec_parent_bit = parents[rand_2][cross_point:]
    print(parents[0])
    print(fst_parent_bit)

    print(f'par 1 {parents[0]} par2 {parents[1]}')
    new_parent1 = parents[rand_1][:cross_point] + sec_parent_bit
    new_parent2 = parents[rand_2][:cross_point] + fst_parent_bit
    print(new_parent1)
    print(new_parent2)
    parents[rand_1] = new_parent1
    parents[rand_2] = new_parent2
    # parents = parents + tuple([(parents[0][0:cross_point + 1] + parents[1][cross_point + 1:ONE_INDIVIDUAL_SIZE - 1])])
    # parents = parents + tuple([(parents[1][0:cross_point + 1] + parents[0][cross_point + 1:ONE_INDIVIDUAL_SIZE - 1])])
    print(f'updated parents {parents}')


def mutation() :
    global populations, parents
    mute = random.randint(0, 49)
    if mute == 20 :
        x = random.randint(0, 1)
        y = random.randint(0, ONE_INDIVIDUAL_SIZE - 1)

        if(parents[x][y] == 1):
            parents[x][y] = 0

        if parents[x][y] == 0:
            parents[x][y] = 1

    populations = parents
    # print(populations)


if __name__ == "__main__":
    # initialize population
    populations = [[random.randint(0, 1) for x in range(ONE_INDIVIDUAL_SIZE)] for i in range(POPULATION_SIZE)]
    print(type(populations))
    parents = []
    # new_populations = []
    # print(populations)
    #
    for i in range(100):
        fitness_score()
        selectparent()
        crossover()
    # mutation()