import random
from simulated_annealing import simulated_annealing
from dimension_range import DimensionRange

def cost(sol):
   x = sol[0]
   y = sol[1]

   error1 = 20 - x - y  # This error will be zero when x+y = 20
   error2 = 362 - x**2 - y ** 2 # this error will be zero when x**2+y**2 = 362

   return error1 ** 2 + error2 ** 2

seed = 150
random.seed(150)
space = [DimensionRange(0, 20), DimensionRange(0, 20)] # Two dimensions
sol = simulated_annealing(seed, space, cost, initial_T = 10.0, final_T = 1.0, cooling_rate = 0.9, max_step = 1)
print("Solution is {}, the cost is {}".format(sol, cost(sol)))
