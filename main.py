import random


class DNA:
  def __init__(self):
    pass


class Population:
  def __init__(self):
    pass


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
