from math import floor
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
  

  def mutate(self):
    for i in range(len(self.genes)):
      if(random.random() < self.mutation_rate):
        self.genes[i] = DNA.make_gene()

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
    self.max_fitness = 0
    self.max_fitness_dna = None
    self.mappingpool = []
  
  def _fitness(self, dna):
    score = 0
    for i in range(len(dna.genes)):
      if(self.target[i] == dna.genes[i]):
        score += 1

    return pow(score / len(self.target), 10)

  def _pickParent(self):
    index = random.randrange(len(self.mappingpool))
    return self.mappingpool[index]

  def selection(self):
    self.fitness = [self._fitness(dna) for dna in self.elements]

    for i in range(len(self.fitness)):
      if self.fitness[i] > self.max_fitness:
        self.max_fitness = self.fitness[i]
        self.max_fitness_dna = self.elements[i]
    print(f"Generation #{self.generation}) {''.join(self.max_fitness_dna.genes)}")

  def reproduction(self):
    self.mappingpool = []
    
    # make a matingpool
    for i in range(len(self.elements)):
      fitness = Utils.rescale(self.fitness[i], 0, self.max_fitness, 0, 1)
      n = floor(fitness * 100)
      for _ in range(n):
        self.mappingpool.append(self.elements[i])

    # new generation
    for i in range(len(self.elements)):
      parent1 = self._pickParent()
      parent2 = self._pickParent()

      child = parent1.crossover(parent2)
      child.mutate()

      self.elements[i] = child
    
    self.generation += 1

  def evaluate(self):
    for dna in self.elements:
      tmp = ''.join(dna.genes)
      if tmp == self.target:
        return f"Generation #{self.generation}) {tmp}"
    
    return False

class Utils:
  @staticmethod
  def rescale(n, start, stop, new_start, new_stop):
    return ((n-start) / (stop-start)) * (new_stop-new_start) + new_start


# parameters
target = "Huzaifa Nimushimirimana a.k.a Kalculta."
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
    break
