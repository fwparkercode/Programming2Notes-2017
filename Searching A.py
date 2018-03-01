# Searching

file = open('data/villains.txt', 'r')


for line in file:
    # strip method removes spaces and \t \n from a string
    print(line.strip())
file.close()


file = open('data/villains.txt', 'r')

for line in file:
    print("Hello", line.strip())

file.close()

# We can also write to a file.
''''
file = open('data/villains.txt', "w")  # overwrites the file

file.write("Lee The Merciless")

file.close()


# appending to a file
file = open('data/villains.txt', 'a')  # append to a file
file.write("\nLee the Merciless")
file.close()
'''

# Read a file into an array (list)

villains = []
file = open('data/villains.txt', 'r')

for name in file:
    villains.append(name.strip())

file.close()
print(villains)

# Linear Search
# find 'The Infamous Devourer"

key = "Vladimir Noir"
i = 0
while i < len(villains) and villains[i] != key:
    i += 1

if i < len(villains):
    print(key, "is at position", i)
else:
    print(key, "is not found")

# Binary Search

key = "Morgiana the Shrew"
lower_bound = 0
upper_bound = len(villains) - 1
found = False

while not found and lower_bound <= upper_bound:
    middle_pos = (upper_bound - lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print("Found", key, "at position", middle_pos)
else:
    print(key, "was not found")

import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("data/villains.txt")
'''
all_words = []
for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)
'''

all_words = [x for line in file for x in split_line(line)]

print(all_words)

player = "X"
if player == "O":
    player = "X"
else:
    player = "O"

#lengths = [len(x) for x in all_words]
# find the max
# find the index of the max
# use the index to find the corresponding word in the list

#print(all_words[lengths.index((max(lengths)))])


for i in range(len(all_words)):
    if all_words[i] == "Rufus":
        print(all_words[i + 1])



