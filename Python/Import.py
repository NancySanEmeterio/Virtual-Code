import math


result = math.sqrt(25)
print(result)  # Prints 5.0

'''We can also import specific functions from a module 
using the syntax from module import function.'''
from math import sqrt


result = sqrt(25)
print(result)  # Prints 5.0

import random
import datetime


random_number = random.randint(1, 10)
print(random_number)  # Prints a random integer between 1 and 10


current_date = datetime.datetime.now()
print(current_date)  # Prints the current date and time