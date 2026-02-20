# Functions is a block of code that performs specific task
# def functionname()


# default function with no parameters
def printdata():
    print("Hello world")

# call the function
printdata()

# functions with parameters
def printdata(name):
    print("Hello " + name)

# pass the arguments
printdata("Avanish")

#return statement
# to return the function value return statement is used

def sq(num):
    result = num * num
    return result
num = 3
square = sq(3)
print(f"Sqaure of {num} is " , square)


# function pass

def func_pass():
    pass

#call the function
func_pass()

# multiple return value

def cal(a, b):
    return a+b, a-b, a*b

add, sub, mul = cal(10, 5)
print(add)
print(sub)
print(mul)

#function calling a another function

def areaofrect(len, width):
    return len * width

def areaofsq(side):
    return side * side

value = areaofrect(4, 6)
print(areaofsq(value))

def even(limit):
    for i in range(2, limit + 1, 2):
        print(i)

even(10)

# function with if else condition
def even(limit):
    if limit % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print(even(10))
print(even(11))