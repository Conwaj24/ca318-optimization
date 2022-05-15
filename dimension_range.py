import math
import random
import optimization

class DimensionRange():
   def __init__(self, mini, maxi):
      self.minimum = mini
      self.maximum = maxi

   def __str__(self):
      return "({}, {})".format(self.minimum, self.maximum)

   def __repr__(self):
      return str(self)

def cost(sol):
   error = 81 - sol[0] ** 2
   return error ** 2 # Square the error ensures it is always positive.
