# 1.Write a Python function to sum all the numbers in a list.

list = [1,2,3,4,5,6,7,8,9,10]

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list(list))

#2.Write a Python function to find the maximum of three numbers.

def max(a, b, c):
    if a>=b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c

print(max(111,22,3))
