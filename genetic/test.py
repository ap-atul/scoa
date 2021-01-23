from genetic import *

## TODO
## 1. Generate random populatio of genome (tuple (x, y))
## 2. Cross over
## 3. Mutation (min = -10, max = 10)
## 4. tournament selection (select random sol, add only the fittest)
## 5. run tour on 2, use them to cross over, then mutate on new pop

sol, fit = run_genetic(10, 100)

print()
print(f"Fitness of the solution :: {rosenbrock(sol)}")
print(f"Solution after evolution :: {sol}")


