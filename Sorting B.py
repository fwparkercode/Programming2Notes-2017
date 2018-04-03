# SORTING
import random

# swap values
a = 1
b = 2
print(a, b)

temp = a  # make a temporary variable to swap
a = b
b = temp
print(a, b)

a, b = b, a  #  Python way (pythonic way that a pythonista would do it)
print(a, b)

# Selection Sort

# make a random list of 100 numbers from 1 to 99
my_list = [random.randrange(100) for x in range(100)]
print(my_list)

for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[min_pos], my_list[cur_pos] = my_list[cur_pos], my_list[min_pos]

print(my_list)

# Insertion Sort

my_list = [random.randrange(100) for x in range(100)]
print(my_list)

for key_pos in range(1, len(my_list)):
    key_value = my_list[key_pos]

    # scan from right to left
    scan_pos = key_pos - 1

    # loop through until we find one smaller
    while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
        my_list[scan_pos + 1] = my_list[scan_pos]
        scan_pos -= 1

    my_list[scan_pos + 1] = key_value

print(my_list)

# Sorting using sort, sorted, and lambda functions.
my_list = [5, 2, 8, 1, 7, 3]
my_list.sort()  # sort in place using sort method
my_list = sorted(my_list) # sorted function
print(my_list)

my_list = [[5, 2], [8, 1], [7, 3]]
my_list.sort()
print(my_list)

# sort and sorted take a function as a parameter
# use a lambda function
# lambda parameters: returned value
square = lambda x: x ** 2
print(square)
print(square(9))

product = lambda x, y: x * y
print(product(7, 8))

# sort/sorted WITH a lambda function
my_list = [[5, 2], [8, 1], [7, 3]]
my_list.sort(key= lambda x: x[1])
print(my_list)






