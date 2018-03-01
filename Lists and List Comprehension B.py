# LISTS AND LIST COMPREHENSIONS

my_list = ["Bev", "abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [8, 4, 7, 5, 2, 9]

# using indices
print(my_list[3])
my_list[3] = "Deb"
print(my_list)

# slicing
print(my_list[3:5])  # prints index 3 and 4
print(my_list[:4])  # beginning to 3
print(my_list[4:])  # 4 to end
print(my_list[:])  # prints the whole list

# copying a list
my_list_copy = my_list  # NOT THIS WAY
my_list_copy[-1] = "Gob" # can use negative indices
print(my_list_copy)
print(my_list)

my_list_copy = my_list[:]  # this copies the whole list into a new one
my_list_copy[-2] = "Feb" # can use negative indices
print(my_list_copy)
print(my_list)

# METHODS (AND FUNCTIONS) FOR LISTS

#finding out if an item exists in a list
print("Deb" in my_list)

# Find the min and max of a list
print(min(my_numlist))
print(max(my_numlist))
print(sum(my_numlist))
print(min(my_list)) # Alphabetical (sort of)  goes by ordinal number
#  print(ord("A"))

# find the index
print(my_list.index("Deb"))

# find how many times an item appears in a list
print(my_list.count("Gob"))

# add to a list
my_list.append("Gob")
print(my_list.count("Gob"))

# insert a value into a list
my_list.insert(3, "Don")
print(my_list)

# sort a list
print(my_list)
my_list.sort()
print(my_list)

# reverse a list
my_list[my_list.index("abe")] = "Abe"
my_list.reverse()
print(my_list)

# clear a list
my_list.clear()
print(my_list)

my_list = my_list_copy[:]  # get my list back

# Pop - removes an item from the list AND returns it
print(my_list)
removed_name = my_list.pop()  # default removes the last item (pops it off)
print(my_list)
print(removed_name)

first_name = my_list.pop(0)  # you can also index it
print(first_name)
print(my_list)

# Delete an item from a list
del my_list[0]
print(my_list)
del my_list[1:]
print(my_list)


# ITERATING
# FOR EACH LOOP - Cannot change the list with this method
for item in my_numlist:
    item *= 2
    print(item)

print(my_numlist)

# Index variable LOOP
for i in range(len(my_numlist)):
    my_numlist[i] *= 2
    print(my_numlist[i])

print(my_numlist)

# CREATE LISTS
# Make a list of numbers 1 to 100
my_list = []
for i in range(1, 101):
    my_list.append(i)

print(my_list)

# Go back through the list and square everything
for i in range(len(my_list)):
    my_list[i] **= 2

print(my_list)



# ITERATING A LIST
#  make a list from 0 to 9
my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)

#  print each item in the list using for each
for item in my_list:
    print(item)

#  add 10 to each item in the list using iteration
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)

# make a 2d list that is 10 x 10   [[0, 0], [0, 1], [0, 2] ... [9, 9]]
my_list = []
for i in range(10):
    for j in range(10):
        my_list.append([i, j])
print(my_list)

# print each pair
for item in my_list:
    print(item)

# add 10 to each y item using iteration
for i in range(len(my_list)):
    my_list[i][1] += 10


# LIST COMPREHENSIONS
# make a list of numbers from 0 to 99 and print it
my_list = []
for i in range(100):
    my_list.append(i)
print(my_list)

# or we can do it this way
my_list = [x for x in range(100)]
print(my_list)


# Square every item in the previous list and print it
for i in range(len(my_list)):
    my_list[i] **= 2
print(my_list)

my_list = [x ** 2 for x in my_list]
print(my_list)

# create the list and square it
my_list = [x ** 2 for x in range(100)]
print(my_list)

# Alter list to show only odd numbers and print it
my_list2 = []
for square in my_list:
    if square % 2 == 1:
        my_list2.append(square)
print(my_list2)

my_list2 = [x for x in my_list if x % 2 == 1]
print(my_list2)


# Alter list to to show only numbers 100 to 1000 and print it
my_list3 = []
for square in my_list2:
    if square >= 100 and square <= 1000:
        my_list3.append(square)
print(my_list3)

my_list3 = [x for x in my_list2 if x >= 100 and x <= 1000]
print(my_list3)

# Do all four at once
# generate a list from 0 to 99
# square it
# only odd between 100 and 1000
my_list = [x ** 2 for x in range(100) if x ** 2 % 2 == 1 and x ** 2 >= 100 and x ** 2 <= 1000]
print(my_list)


# list comprehension
# [appended-to-list  for  iterator  in range_or_list  filter]

# roll a single die 100 times and put in list
import random
rolls = [random.randrange(1, 7) for x in range(100)]
print(rolls)

# roll two dice in pairs 100 times and put in a list
rolls = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(rolls)

# create a list of only the doubles from my_rolls
doubles = [x for x in rolls if x[0] == x[1]]
print(doubles)

# can we generate a list and filter doubles on single line
doubles = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for y in range(100)] if x[0] == x[1]]
print(doubles)




'''
print("Francis Parker".lower())

name = "Francis Parker"

for char in name:
    print(char.lower(), char)


number = int(input("Enter an int"))
print(4 + number)

if 3 != 4:
    print("Yep")

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                num = int(str(d) + str(c) + str(b) + str(a))
                print(num)

print(sum([2, 3, 4]))

def sum_product(n1, n2):
    sum = n1 + n2
    
'''
