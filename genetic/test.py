from genetic import *

sol, fit = run_genetic(pop_size=100, gen_size=10, disp=True)

print()
print(f"Fitness of the solution :: {rosenbrock(sol)}")
print(f"Solution after evolution :: {sol}")


