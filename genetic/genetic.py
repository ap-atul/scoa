import random
import math

def rosenbrock(x): # https://www.sfu.ca/~ssurjano/rosen.html
    return sum([ ( 100 * math.pow((x[i + 1] - math.pow(x[i], 2)), 2) + math.pow((x[i] - 1), 2)  )  for i in range(len(x) - 1)])

MIN, MAX = -10, 10
MUTATION = 0.4
TOURNEY = 4

def get_rand(lower=MIN, higher=MAX):
    return random.randrange(lower, higher)

def gen_rand_population(pop_size=100, dim=2):
    return [[get_rand() for _ in range(dim)] for _ in range(pop_size)]

def crossover(one, two):
    assert len(one) == len(two)
    r = random.randint(0, len(one))
    return one[r: ] + two[0: r], one[0: r] + two[r: ]

def mutate(one):
    if (r :=  get_rand(0, 1)) == MUTATION:
        one[r] = get_rand()
    return one

def fitness(one):
    return rosenbrock(one)

def tournament(pop):
    tourn = list()
    for _ in range(TOURNEY):
        r = get_rand(0, len(pop))
        tourn.append(pop[r])

    fitnesses = [fitness(genome) for genome in tourn]
    return pop[fitnesses.index(max(fitnesses))]

def get_best(pop):
    fitnesses = [fitness(genome) for genome in pop]
    return pop[fitnesses.index(max(fitnesses))], max(fitnesses)

def run_genetic(pop_size, gen_size, disp=True):
    result = list()
    best_fitness = None
    best_solution = None

    pop = gen_rand_population(pop_size)
    best_solution, best_fitness = get_best(pop)
    for i in range(gen_size):
        pop = sorted(pop, key=lambda gene: fitness(gene))

        new_pop = pop[0: 2]

        if disp:
            print(f"Generation :: {i}")

        for i in range(int(len(pop) / 2) - 1):
            parent1 = tournament(pop)
            parent2 = tournament(pop)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_pop.append(child1)
            new_pop.append(child2)

            sol, fit = get_best(pop)
            if fit > best_fitness:
                best_solution, best_fitness = sol, fit

            if disp:
                print(f"Population len:: {len(pop)}, Fitness :: {fit}")

        pop = new_pop

    return best_solution, best_fitness


