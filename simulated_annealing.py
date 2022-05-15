import random
import math

def get_small_random_change(current, space, max_step = 1):
   random_index = random.randint(0, len(space)-1)

   # Choose a direction to change it
   random_step = random.randint(1, max_step)
   # Possibly negative
   if random.random() < 0.5:
      random_step = -random_step

   # Create a new list with one of the values changed
   new = current[:]
   new[random_index] += random_step
   if new[random_index] < space[random_index].minimum: # too small? ...
      new[random_index] = space[random_index].minimum # ... fix
   elif new[random_index] > space[random_index].maximum: # too big ...
      new[random_index] = space[random_index].maximum

   return new

def simulated_annealing(seed, space, cost, initial_T = 100.0, final_T = 0.1, cooling_rate = 0.99, max_step = 1):
   # Initialize the values randomly
   random.seed = (seed)
   current = [random.randint(space[i].minimum, space[i].maximum) for i in range(len(space))]

   for step in range(max_step, 0, -1):
      T = initial_T

      while T > final_T:
         # Choose one of the dimension
         new = get_small_random_change(current, space, step)

         # Is it better ...
         delta = cost(new) - cost(current)
         if delta < 0:
            # ... yep, better, let's take it.
            current = new 
         else:
            # Not better, should we chance it anyway?
            probability = math.e ** (-delta / T) # use the Boltzmann function
            if random.random() < probability:
               current = new # The man from Boltzmann says yes.

         # Decrease the temperature for the next cycle
         T = T * cooling_rate

   return current
