# LOOPS AND RANDOM NUMBERS

# FOR LOOPS

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(-5, 5):
    print(i)

for i in range(5, 15, 3):
    print(i)

# RANDOM NUMBERS
import random

print(random.randrange(10))  # random INT 0 to 9
print(random.randrange(5, 16))  # 5 to 15
print(random.randrange(-5, 5))  # -5 to 4
print(random.randrange(5, 15, 3))  # 5 to 14 by 3s (5, 8, 11, 14)
print(random.randrange(10, -11, -2))

print(random.random())  # random FLOAT from 0 to 1
print(random.random() * 10 + 5)  # random FLOAT from 5 to 15

# BREAK
# immediately exits (breaks out of) the current loop.
# keep rolling a die until you get a 6
for i in range(100):
    roll = random.randrange(1, 7)
    print("You rolled a", roll, "on roll number", i)
    if roll == 6:
        break

# CONTINUE
# skips the rest of the current iteration
for i in range(10):
    roll = random.randrange(1, 7)
    if roll % 2:
        continue
    print(roll)


# FOR ELSE
# if you make it all the way through the FOR loop without breaking
# then you do the ELSE statement

for i in range(10):
    n = random.randrange(10)
    print(n)
    if n == 0:
        break
else:
    print("Did not roll a zero")

print(37.58 % .25)


word = "dog"

for letter in word:
    print(bin(ord(letter)))

print(0b1001 + 0b0010)

print("{} dollars {} quarters".format(1, 2))
