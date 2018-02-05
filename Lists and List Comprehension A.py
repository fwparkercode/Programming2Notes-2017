# Lists

my_list = ["Bev", "Abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [8, 4, 7, 5, 2, 9]

print(my_list[0]) # single index
print(my_list[-3:-1])  # multiple items, first one included, last one not

# copy of a list
my_newlist = my_list[:]
my_newlist[3] = "Deb"
print(my_newlist)
print(my_list)

# 2d list
my_2dlist = [["Abe", 8], ["Bev", 4], ["Cam", 7]]
print(my_2dlist[2][0])

# if in
if "Cam" in my_list:
    print("Cam is on the list")

# list functions
# for strings, order is alphabetical (sort of)
print(min(my_list))  # smallest value
print(max(my_list))  # largest value
print(sum(my_numlist))  # sums a list

# list methods
my_list.append("Abe")
print(my_list.count("Abe"))  # finds number of times an item appears
my_list.insert(2, "Evelyn")

my_list.sort()
my_numlist.sort()
print(my_list)
print(my_numlist)

my_list.reverse() # reverse sort
print(my_list)

my_list.pop()  # pops off the last one in the list
print(my_list)
my_list.pop(2)  # pops off the second item
print(my_list)
first_in_line = my_list.pop(0)  # returns the popped value
print(first_in_line)
print(my_list)

del my_list[0:2]  # look this one up
print(my_list)

print(my_list.index("Cam"))

#name = input("Enter your username: ")
#print(name)

import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start = time.clock()
        result = self.func(*args, **kargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print("{}:\telapsed: {}\ttime:{}".format(self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), rannge(N)))

result = listcomp(3)
listcomp(10000)

print(result)


def hello(name):
    return "Hello {}.".format(name)

hello_list = map(hello, my_list)
for hello in hello_list:
    print(hello)


hello_list = [x + "!" for x in my_list]
print(hello_list)