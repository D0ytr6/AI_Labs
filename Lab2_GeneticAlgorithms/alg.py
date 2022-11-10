import math
import numpy as np # linear algebra
import os
import random

POPULATION_SIZE = 8
ONE_INDIVIDUAL_SIZE = 8
MAX_GENERATION = 50
pt_crossover = 0.61
pm_mutation = 0.01

best = -100000

# fitness score calculation ............
def fitness_score():
    global populations, best
    fit_value = []
    fit_score = []
    for i in range(POPULATION_SIZE):
        chromosome_value = 0
        for j in range(ONE_INDIVIDUAL_SIZE - 1, -1, -1):
            chromosome_value += populations[i][j] * (2 ** (7 - j))
        print(f'chromosome_value in 10 system = {chromosome_value}')
        func_result = - (math.pow((chromosome_value - 1), 2) / 256)
        print(f'func res = {func_result}')
        fit_value.append(func_result)

    print(fit_value)
    #     chromosome_value = -1 * chromosome_value if populations[i][0] == 1 else chromosome_value
    #     print(chromosome_value)
    #     fit_value.append(-(chromosome_value ** 2) + 5)
    # print(fit_value)
    # fit_value, populations = zip(*sorted(zip(fit_value, populations), reverse=True))
    # best = fit_value[0]




if __name__ == "__main__":

    # initialize population
    populations = ([[random.randint(0, 1) for x in range(ONE_INDIVIDUAL_SIZE)] for i in range(POPULATION_SIZE)])
    print(type(populations))

    parents = []
    new_populations = []
    print(populations)

    fitness_score()