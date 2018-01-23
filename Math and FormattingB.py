# MATH

# floats vs ints
my_int = 1
my_float = my_int / 2

print(my_int, my_float)

print(1.2 / 2 + 1.2)

# VARIABLES
# Naming
snake_case = "Lower case with underscores between words."
camelCase = "New words are capitalized."

# Not allowed
# tax% = 0.05           # No special characters allowed
# 8ball = 8             # Cannot start with a number
# ball8 = 8             # This is allowed
# my.variable = True    # no dot notation
# my variable = False   # no spaces

# Assignment operator - Equal sign
# The ONLY way to change a variable (sort of)
x = 5
x + 1
print(x)

x = x + 1
print(x)

# MATH OPERATORS
# + - * /
# **     # exponent
# //     # floor division, similar to int(), rounds down
print(3.8 // 2)  # divides and chops off the decimal remainder
print(int(3.8 / 2))

# % modulo, remainder after division
print(7 % 2)  # 1
print(11 % 7)  # 4

# COMPOUND ASSIGNMENT OPERATORS
# += -= *= /=
y = 1
y += 1  # y = y + 1
print(y)

y *= 3
print(y)

y **= 2
print(y)

# ROUND FUNCTION
x = 1234.5678
print(round(x, 2))

# FORMAT  "{}".format()
# for formatting TEXT
# Position:PlaceholderJustificationWidthDecorationsType

# Let's format some text
first = "Jerry"
last = "Garcia"

invite_list = [["Abe", "Anderson"], ["Bev", "Beverly"], ["Cam", "Carter"]]

for person in invite_list:
    print("{} {}, would you like to come to my party.".format(person[0], person[1]))

# print the first name
print("{}".format(first))

# print first last
print("{} {}".format(first, last))

# print     First: first     Last: last
print("First: {} \tLast: {}".format(first, last))

# print last, first
print("{1}, {0}".format(first, last))




# Number formatting works similarly
# You may specify d for digit/int, f for float, e for exponent to force a format
# here are some common uses

# round a float to a decimal place   {:.3f} rounds to 3
pi = 3.1415926535897932348

print("{:.5f}".format(pi))


# add a sign to a number {:+}
# this works for positive and negative numbers (both use +)
print("{:+}".format(pi))

# add comma formatting to number {:,}
my_number = 1187923978123
print("{:,}".format(my_number))


# right align :>x where x is the width of text
print("{:>30}".format(pi))
# left align :<x
print("{:<30}".format(pi))
# center align :^x
print("{:^30}".format(pi))

# percent {:%} {:.2%}
print("{:>20}".format(0.578))


# exponent {:e} {:.2e}

# leading zero (or other placeholder) {:05}

# dollars and cents?
# 142.3  >> $142.30


# Make a github account.  Use a name I will recognize.
# I don't want an assignment coming from chidog843
