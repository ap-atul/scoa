import random

def rosenbrock(x, y):
    return abs((1- x) ** 2 + 100 * (y - x ** 2) ** 2)

MIN, MAX = -10, 10
MUTATION = 0.4
TOURNEY = 4

def get_rand(lower=MIN, higher=MAX):
    return random.randrange(lower, higher)

def gen_rand_population(pop_size=100):
    return [(get_rand(), get_rand()) for _ in range(pop_size)]

def crossover(one, two):
    assert len(one) == len(two)
    r = random.randint(0, 1)
    n = random.randint(0, 1)
    return (one[r], two[n]), (two[r], one[n])

def mutate(one):
    if get_rand(0, 1) == MUTATION:
        print("mutating this shit")
        return (get_rand(), one[random.randint(0, 1)])
    return one

def fitness(one):
    return rosenbrock(one[0], one[1])

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
        pop = sorted(pop, key=lambda gene: fitness(gene), reverse=True)

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


