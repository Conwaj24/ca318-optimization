from random import randint

def random_optimize(space, cost, steps=1000):
   # Get a random solution
   random_sol = [randint(space[i].minimum, space[i].maximum) for i in range(len(space))]
   best_so_far = random_sol

   for j in range(1, steps):
      # Create a random solution
      random_sol = [randint(space[i].minimum, space[i].maximum) for i in range(len(space))]
    
      # is this better than our best so far
      if cost(random_sol) < cost(best_so_far):
         best_so_far = random_sol

   return best_so_far