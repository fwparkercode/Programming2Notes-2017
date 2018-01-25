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
# %      # modulo, remainder after division


# COMPOUND ASSIGNMENT OPERATORS
# += -= *= /=


# ROUND
x = 1234.5678


# FORMAT  "{}".format()
# for formatting TEXT
# Position:PlaceholderJustificationWidthDecorationsType

# Let's format some text
first = "Jerry"
last = "Garcia"
print(first, last)
print(first + last)

# print the first name
print("{}".format(first))

# print first last
print("My name is {} {}.".format(first, last))

# print     First: first     Last: last
print("First: {}\t\tLast: {}".format(first, last))


# print last, first
print("{1}, {0}".format(first, last))


# Number formatting works similarly
# You may specify d for digit/int, f for float, e for exponent to force a format
# here are some common uses

# round a float to a decimal place   {:.3f} rounds to 3
pi = 3.1415926535897
print("{:.3f}".format(pi))

# add a sign to a number {:+}
# this works for positive and negative numbers (both use +)
print("{:+}".format(pi))

# add comma formatting to number {:,}
my_number = 679342678
print("{:,}".format(my_number))

# right align :>xd where x is the width of text
print("{:>20}".format(first))

# left align :<xd
print("{:<20}".format(first))

# center align :^xd
print("{:^20}".format(first))

# percent {:%} {:.2%}
print("{:.2%}".format(0.973))

# exponent {:e} {:.2e}
print("{:.2e}".format(234234.234))

mole = 6.02e23

# leading zero (or other placeholder) {:05}
print("{:+020}".format(234))


# dollars and cents?
# 142.3  >> $142.30
print("${:.2f}".format(142.3))


# Make a github account.  Use a name I will recognize.
# I don't want an assignment coming from chidog843

# Github is...
# a Version Control System (VCS)
# a place to collaborate with other programmers
# a publishing tool
# a social media site


# Allows many people to work on same file without work being lost or edited.
# Files can be tracked and merged together.
# It is a "time machine" if you want to revert to a previous version of your code.
# Files are stored in repositories
# Acts in the cloud.
# Reads any language

# repository - where the project files are stored (repo)
# master - repository main branch (where integration happens)
# clone - copy of existing repo.  From github repo to local repo.
# commit - submit file to local repo.
# pull (update) - grab the latest code from the repo
# push - submit code to a remote repo (from local to github)
# head - reference to the node where the repo points (most current official update)

#### Let's do branches and merges later in the semester.