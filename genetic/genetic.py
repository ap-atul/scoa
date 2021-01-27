from matplotlib import pyplot as plt
import random
import math

MIN, MAX = -2, 2
MUTATION = 0.5
TOURNEY = 4

def rosenbrock(x): # https://www.sfu.ca/~ssurjano/rosen.html
    return sum([ ( 100 * math.pow((x[i + 1] - math.pow(x[i], 2)), 2) + math.pow((x[i] - 1), 2)  )  for i in range(len(x) - 1)])

def get_rand(lower=MIN, higher=MAX):
    return random.randrange(lower, higher)

def gen_rand_population(pop_size=100, dim=10):
    return [[get_rand() for _ in range(dim)] for _ in range(pop_size)]

def crossover(one, two):
    assert len(one) == len(two)
    r = random.randint(0, len(one))
    return one[r: ] + two[0: r], one[0: r] + two[r: ]

def mutate(one):
    if random.uniform(0, 2) <= MUTATION:
        one[random.randint(0, len(one) - 1)] = get_rand()
    return one

def fitness(one):
    return rosenbrock(one)

def tournament(pop):
    tourn = [pop[get_rand(0, len(pop))] for _ in range(TOURNEY)]
    fitnesses = [fitness(genome) for genome in tourn]
    return pop[fitnesses.index(max(fitnesses))]

def get_best(pop):
    fitnesses = [fitness(genome) for genome in pop]
    return pop[fitnesses.index(max(fitnesses))], max(fitnesses)

def run_genetic(pop_size, gen_size, disp=True):
    pop = gen_rand_population(pop_size)
    best_solution, best_fitness = get_best(pop)
    fitnesses = list()
    for i in range(gen_size + 1):
        pop = sorted(pop, key=lambda gene: fitness(gene), reverse=True)
        new_pop = pop[0: 2]

        if disp:
            print(f"\nGeneration :: {i}")
        for i in range(int(len(pop) / 2) - 1):
            parent1, parent2 = tournament(pop), tournament(pop)
            child1, child2 = crossover(parent1, parent2)
            child1, child2 = mutate(child1), mutate(child2)
            new_pop += [child1, child2]
            sol, fit = get_best(pop)
            fitnesses.append(fit)
            if fit > best_fitness:
                best_solution, best_fitness = sol, fit
        if disp:
            print(f"  Population fitness :: {fit}")
        pop = new_pop

    plt.plot(fitnesses)
    plt.show()
    return best_solution, best_fitness
