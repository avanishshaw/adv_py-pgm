#
# Q1 What is the output?

a = list(enumerate(['a', 'b', 'c']))
print(a)

# Output - [(0, 'a'), (1, 'b'), (2, 'c')]


# Q2 What is the output?

for i, v in enumerate([10, 20, 30]):

    print(i, v)

# Output - 0 10
#          1 20
#          2 30

# Q3 Write code to print index + value from:

colors = ['red', 'green', 'blue']
for i, color in enumerate(colors, start=1):
    print(i, color)
# Index should start from 1.


# Q4 What is the output?

py = list(enumerate("PYTHON", start=1))
print(py)
# Output-[(1, 'P'), (2, 'Y'), (3, 'T'), (4, 'H'), (5, 'O'), (6, 'N')]


# Q5 Find the index of value 50 using enumerate():

nums = [10, 20, 30, 40, 50, 60]
for i, v in enumerate(nums):
    if v == 50:
        print(i)
# Q6 What is the output?

for i, n in enumerate(range(10, 60, 10)):

    print(i, n)
# Output-
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50

# Q7 Convert this into an enumerate() loop:

# for i in range(len(data)):
#     print(i, data[i])
data = [1,2,3,4,5]
for i, value in enumerate(data):
    print(i, value)

# Q8 What is printed?

items = ['a', 'b', 'c']

for i in enumerate(items):
    print(i)

#Printed
# (0, 'a')
# (1, 'b')
# (2, 'c')

# Q9 What is the output?

val = list(enumerate([], start=5))
print(val)
# Output - []

# Q10 What is the output?

for i, v in enumerate([100, 200, 300], start=-1):

    print(i, v)
#Output -
# -1 100
# 0 200
# 1 300


# Q11 What happens here?

# i, v = enumerate(['x', 'y', 'z'])

# Output - Error
# i, v = enumerate(['x', 'y', 'z'])
#     ^^^^
# ValueError: too many values to unpack (expected 2)


# Q12 Explain the difference:

enumerate(data)
# Indexing starts with default i.e 0
enumerate(data, start=1)
# Indexing starts with 1 as defined
