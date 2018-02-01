from math import *  # * is a wildcard
from random import randrange

from my_imports import my_import

square = 1

# Functions
def my_function(name):
    '''
    Says hello
    :param name: 
    :return: 
    '''
    x = 2
    print("Square =", square)
    print("Hello", name)

#my_function("Mr. Lee") # this will always run on execution or import

def square_cube(n):
    '''
    returns square and cube of the number
    :param n: 
    :return: square, cube 
    '''
    square = n ** 2
    cube = n ** 3
    print("Square =", square)
    my_import.product_sum(square, cube)
    return square, cube


if __name__ == "__main__":
    # this is the file that you executed/ran
    my_function("Mr. Lee")
    my_import.product_sum(10, 20)
    print(randrange(100))
    print(e)
    print(pi)
    sqr_cube = square_cube(7)
    print(sqr_cube[0], sqr_cube[1])
    sqr, cube = square_cube(8)
    print(sqr, cube)
    #print(x)

    # Scope rules
    # python (__main__), global (far left), local (inside functions)
    # you can see a global variable anywhere, but cannot change it locally.
    # you can ONLY see a local variable locally.  Local variables do not exist outside namespace




