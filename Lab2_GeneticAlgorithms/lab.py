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
        super(Individual, self).__init__(*args)
        self.fitness = FitnessMax()

def oneMaxFitness(individual):
    pass

def create_individual():
    individual = Individual( )