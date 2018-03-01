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


# ITERATING A LIST
#  make a list from 0 to 9
my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)


#  print each item in the list using for each
for num in my_list:
    num += 1
    print(num)
print(my_list)

#  add 10 to each item in the list using iteration
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)

# make a 2d list that is 10 x 10   [[0, 0], [0, 1], [0, 2] ... [9, 9]]
my_list = []
for x in range(10):
    for y in range(10):
        my_list.append([x, y])
print(my_list)

# print every pair
for pair in my_list:
    print(pair)


# add 10 to each item using iteration
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i][j] += 10

print(my_list)




# make a list of numbers from 0 to 99 and print it
my_list = []
for i in range(100):
    my_list.append(i)

# Square every item in the previous list and print it
for i in range(len(my_list)):
    my_list[i] **= 2

print(my_list)

# Alter list to show only odd numbers and print it
my_list2 = []
for i in range(len(my_list)):
    if my_list[i] % 2 == 1:
        my_list2.append(my_list[i])

print(my_list2)

# Alter list to to show only numbers 100 to 1000 and print it
my_list3 = []
for i in range(len(my_list2)):
    if my_list2[i] >= 100 and my_list2[i] <= 1000:
        my_list3.append(my_list2[i])

print(my_list3)

# Do all four at once
my_list4 = []
for i in range(100):
    num = i ** 2
    if num % 2 == 1:
        if num >= 100 and num <= 1000:
            my_list4.append(num)

print(my_list4)


# list comprehension
# [returned_item  for  iterator  in range_or_list  filter]

my_list = [x for x in range(100)]
print(my_list)

my_list = [x ** 2 for x in range(100)]
print(my_list)

my_list = [x ** 2 for x in range(100) if x ** 2 % 2 == 1]
print(my_list)

my_list2 = [x for x in my_list if x >= 100 and x <= 1000]
print(my_list2)

# roll a single die 100 times and put in list
import random
my_rolls = [random.randrange(1, 7) for x in range(100)]
print(my_rolls)

# roll two dice in pairs 100 times and put in a list
my_rolls = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_rolls)

# create a list of only the doubles from my_rolls
my_doubles = [x for x in my_rolls if x[0] == x[1]]
print(my_doubles)

# can we generate a list and filter doubles on single line
my_doubles = [y for y in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if y[0] == y[1]]
print(my_doubles)


values = ["2", "3", "4", "5", "6", "7", "8","9", "10", "J", "K", "Q", "K"]
suits = ["H", "S", "C", "D"]

deck = []
for val in values:
    for suit in suits:
        deck.append(val + suit)
print(deck)

shuffled_deck = random.shuffle(deck)
print(shuffled_deck)
print(len(deck))

playerx = False
print(playerx)
playerx = not playerx
print(playerx)


import random
my_list = [11, 12, 13]
print(random.choice(my_list))
print(my_list[random.randrange(len(my_list))])

random.shuffle(my_list)
print(my_list)