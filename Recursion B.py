# RECURSION (Function calling itself)

# functions can call functions

def f():
    print("f")
    g()
def g():
    print("g")

f()

# functions can also call themselves

def hello(count):
    print("hello", count)
    hello(count + 1)

# hello(1)


# controlling recursive functions

def controlled(depth):
    print(depth)
    if depth > 0:
        controlled(depth - 1)


controlled(900)


# factorial

n = 10  # find the factorial
total = 1

for i in range(1, n + 1):
    total *= i

print(total)


# recursive factorial

def recursive_factorial(n):
    if n > 1:
        return n * recursive_factorial(n - 1)
    else:
        return n

print(recursive_factorial(10))