import random


class DNA:
  def __init__(self, size, mutation_rate):
    self.genes = [DNA.make_gene() for _ in range(size)]
    self.size = size
    self.mutation_rate = mutation_rate

  def crossover(self, partener):
    child = DNA(len(self.genes), self.mutation_rate)
    midpoint = random.randrange(len(self.genes))

    for i in range(len(self.genes)):
      if i > midpoint:
        child.genes[i] = self.genes[i]
      else:
        child.genes[i] = partener.genes[i]
    
    return child

  @staticmethod
  def make_gene():
    hex_code = random.randrange(63, 123)

    if hex_code == 63: 
      hex_code = 32
    if hex_code == 64:
      hex_code = 46
    
    return chr(hex_code)

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
