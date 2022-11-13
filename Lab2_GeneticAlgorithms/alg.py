import math
import os
import random
import matplotlib.pyplot as plt

POPULATION_SIZE = 8
ONE_INDIVIDUAL_SIZE = 8
MAX_GENERATION = 50
pt_crossover = 0.61
pm_mutation = 0.01

fit_value = []

def getMiddleParents(values):
    sum = 0
    for value in values:
        sum += value

    sum = sum / POPULATION_SIZE
    return sum


# fitness score calculation ............
def fitness_score():
    global populations
    global fit_value, best_values
    best = 0
    fit_value = []
    for i in range(POPULATION_SIZE):
        chromosome_value = 0
        for j in range(ONE_INDIVIDUAL_SIZE - 1, -1, -1):
            chromosome_value += populations[i][j] * (2 ** (7 - j))
        print(f'chromosome_value in 10 system = {chromosome_value}')
        func_result = - (math.pow((chromosome_value - 1), 2) / 256)
        print(f'func res = {func_result}')
        fit_value.append(func_result)

    # sorting to grow
    fit_value, populations = zip(*sorted(zip(fit_value, populations), reverse=True))
    populations = list(populations)
    fit_value = list(fit_value)
    sum_fit = getMiddleParents(fit_value)
    best_values.append(sum_fit)
    best = fit_value[0]
    # best_values.append(best)
    # print(type(populations))
    print(f'fit_value {fit_value}')
    print(f'population {populations}')
    print(f'best value {best}')


def selectparent():
    global parents, fit_value, populations
    parents = []
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

    # Формуємо нову популяцію батьків для схрещування, розмір рівний розміру популяції
    # Батьки можуть повторятися
    for count in range(POPULATION_SIZE):
        # Крутимо рулетку, отримуємо число
        rand_numb = random.uniform(0, 1)
        individual_number = 0  # Номер батька
        # Перевіряємо співпадання числа з батьком
        for number_parent, score in enumerate(cumulative_fitness_value):
            if rand_numb <= score:
                # Додаємо батька у сформований список
                parents.append(populations[-(number_parent + 1)])
                break

        individual_number += 1

    print(f'parents len {len(parents)}')
    # for i in range(POPULATION_SIZE):
    #     chromosome_value = 0
    #     for j in range(ONE_INDIVIDUAL_SIZE - 1, -1, -1):
    #         chromosome_value += parents[i][j] * (2 ** (7 - j))
    #     print(f'chromosome_value in 10 system = {chromosome_value}')


def crossover2():
    global parents, fit_value


def crossover():
    global parents
    #
    pairs_count = int(len(parents) / 2)
    for pair in range(pairs_count):
        chanse_cross = random.randint(0, 100)
        if(chanse_cross <= 61):
            # Вибираємо точку для одноточкового обміну
            cross_point = random.randint(0, ONE_INDIVIDUAL_SIZE - 1)
            rand_1 = random.randint(0, 7)  # Перший батько
            rand_2 = random.randint(0, 7)  # Другий батько
            while rand_1 == rand_2:  #
                rand_2 = random.randint(0, 7)

            # Формуємо частини для обміну
            fst_parent_bit = parents[rand_1][cross_point:]
            sec_parent_bit = parents[rand_2][cross_point:]

            print(f'par 1 {parents[rand_1]} par2 {parents[rand_2]}')

            # Створюємо нових батьків
            new_parent1 = parents[rand_1][:cross_point] + sec_parent_bit
            new_parent2 = parents[rand_2][:cross_point] + fst_parent_bit

            # Видаляємо старих батьків, ті що не розмножилися залишаються в списку
            if (rand_2 > rand_1):
                parents.remove(parents[rand_2])
                parents.remove(parents[rand_1])
            else:
                parents.remove(parents[rand_1])
                parents.remove(parents[rand_2])

            # Додаємо нових
            parents.append(new_parent1)
            parents.append(new_parent2)

            print(f'updated parents {parents}')


def mutation():
    global populations, parents
    mute = random.randint(0, 100)
    if mute <= 10:
        x = random.randint(0, POPULATION_SIZE - 1)
        y = random.randint(0, ONE_INDIVIDUAL_SIZE - 1)

        if parents[x][y] == 1:
            parents[x][y] = 0
            print(f'Muted bit {parents[x][y]} in parent{parents[x]}')

        if parents[x][y] == 0:
            parents[x][y] = 1
            print(f'Muted bit {parents[x][y]} in parent{parents[x]}')

    populations = parents


if __name__ == "__main__":
    # initialize population
    populations = [[random.randint(0, 1) for x in range(ONE_INDIVIDUAL_SIZE)] for i in range(POPULATION_SIZE)]
    parents = []
    best_values = []
    for i in range(200):
        fitness_score()
        selectparent()
        crossover()
        mutation()

    print(best_values)
    plt.plot(best_values, color="red")
    plt.xlabel('Покоління')
    plt.ylabel('Середня пристосованість')
    plt.title('Середня пристосованість в залежності від покоління')
    plt.show()
