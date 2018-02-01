''''
Function and Module Notes
v1.0
by Aaron Lee
'''
from random import * # random is a library or module, * is the wildcard
# import math  # imports go at the top of your program
from math import pi
# from math import *
import my_module

# when you use keyword from, you are importing directly into your file
# (no need to use random.randrange, just use randrange)

# Functions and Modules
print(randrange(900, 1000))

if __name__ == "__main__":
    '''
    This code only runs if this is the executed code/file.
    '''
    print(randrange(100))
    print(random())
    print(pi)

    e = 5
    print(e)
    print("This is period", my_module.period)
    my_module.hello("Mr. Lee")
    product, sum = my_module.product_sum(10, 20)
    print(product, sum)

