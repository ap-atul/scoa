import random

def rosenbrock(x, y):
    return abs((1- x) ** 2 + 100 * (y - x ** 2) ** 2)

class Genetic:
    def __init__(
            self,
            gensize=100,
            gencount=100,
            bounds=[-100, 100],
            mutation_rate=0.2
        ):
        self._gensize = gensize
        self._gencount = gencount
        self._bound = bounds
        self._mutation = mutation_rate


    def rand_generation(self):
        generation = list()
        for _ in range(self._gensize):
            random_pnt = (random.randint(self._bound[0], self._bound[1]), random.randint(self._bound[0], self._bound[1]))
            generation.append(random_pnt)
        return generation

    def inverse(self, val):
        return 1 if val == 0 else 1 / val

    def fitness(self, solution):
        return self.inverse(rosenbrock(solution[0], solution[1]))

    def probability(self, fitness_score, total):
        assert total != 0
        return fitness_score / total

    def weighted_choice(self, items):
        weighted_total = sum(item[1] for item in items)
        n = random.uniform(0, weighted_total)
        for item, weight in items:
            if n < weight:
                return item
            n -= weight
        return item

    def crossover(self, sol1, sol2):
        pos = 1
        return sol1[: pos] + sol2[pos: ], sol2[: pos] + sol1[pos: ]

    def mutate(self, solution):
        tmp_sol = [solution[0], solution[1]]
        for i in range(len(solution)):
            if random.random() > self._mutation:
                tmp_sol[i] = random.randint(self._bound[0], self._bound[1])
        mutated_sol = (tmp_sol[0], tmp_sol[1])
        return mutated_sol

    def run(self):
        generations, current_gen = list(), 0

        gen = self.rand_generation()
        fitness_scores = [self.fitness(sol) for sol in gen]
        total_val = sum(fitness_scores)
        probabilities = [self.probability(score, total_val) for score in fitness_scores]
        weighted_gen = [((sol[0], sol[1]), probabilities[i]) for i, sol in enumerate(gen)]

        gen = list()
        for _ in range(len(weighted_gen)):
            parent1 = self.weighted_choice(weighted_gen)
            parent2 = self.weighted_choice(weighted_gen)

            child1, child2 = self.crossover(parent1, parent2)

            child1 = self.mutate(child1)
            child2 = self.mutate(child2)

            gen.append(child1)
            gen.append(child2)

        generations.append(gen)

        fittest = self.fitness(generations[0][0])
        sol = generations[0][0]
        for gen in generations:
            fitness_scores = [self.fitness(sol) for sol in gen]

            for score in fitness_scores:
                if score >= fittest:
                    fittest = score
                    sol = gen[fitness_scores.index(score)]

        print(fittest)
        print(sol)



