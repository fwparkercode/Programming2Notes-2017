# Recursion (Functions calling itself)


# Functions calling functions
def f():
    g()
    print("f")


def g():
    print("g")

f()

# Functions calling themselves


def hello():
    print("Hello")
    hello()

#hello()

# We can control the recursion depth
def controlled(level, end_level):
    print("Recursion level", level)
    if level < end_level:
        controlled(level + 1, end_level)

controlled(1, 20)


# Factorial

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

#print(factorial(4))


def recursive_factorial(n):

    if n > 1:
        return n * recursive_factorial(n - 1)
    else:
        return n

print(factorial(5))




