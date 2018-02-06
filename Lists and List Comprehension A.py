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
#  print each item in the list using for each
#  add 10 to each item in the list using iteration


# make a 2d list that is 10 x 10   [[0, 0], [0, 1], [0, 2] ... [9, 9]]
# print every pair
# add 10 to each item using iteration


# make a list of numbers from 0 to 99 and print it

# Square every item in the previous list

# Show only odd numbers

# Show only numbers from 100 to 1000

# Do all four at once

# list comprehension
# [returned_item  for  iterator  in range_or_list  filter]




