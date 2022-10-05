import random


class DNA:
  def __init__(self, size, mutation_rate):
    self.genes = []
    self.size = size
    self.mutation_rate = mutation_rate

  def crossover(self, partener):
    pass


class Population:
  def __init__(self, target, size, mutation_rate):
    self.elements = [DNA(len(target), mutation_rate) for _ in range(size)]
    self.target = target
    self.generation = 0
    self.fitness = []


class Utils:
  @staticmethod
  def rescale(n, start, stop, new_start, new_stop):
    pass


# parameters
target = "No matter where you go know that you not alone."
population_size = 300
mutation_rate = 0.01


# initialization
population = Population(target, population_size, mutation_rate)

# evolution
while True:
  population.selection()
  population.reproduction()

  test = population.evaluate()

  if test:
    print(test)
    print("Best generation: ", population.generation)
    break
