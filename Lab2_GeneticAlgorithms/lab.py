import random

#
POPULATION_SIZE = 8

#
ONE_INDIVIDUAL_SIZE = 8

#
MAX_GENERATION = 50

pt_crossover = 0.61
pm_mutation = 0.01


class FitnessMax():
    def __init__(self):
        self.values = [0]


class Individual(list):
    def __init__(self, *args):
        super(Individual, self).__init__(*args)  # send list param to parent
        self.fitness = FitnessMax()


def oneMaxFitness(individual):
    pass

def create_individual():
    individual = Individual([random.randint(0, 1) for i in range(ONE_INDIVIDUAL_SIZE)])
    return individual

def create_population_list():
    population = list(create_individual() for i in range(POPULATION_SIZE))
    return population

if __name__ == "__main__":
    population = create_population_list()
    print(population)
