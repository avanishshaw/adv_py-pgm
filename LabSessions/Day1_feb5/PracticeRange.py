# 1.Write a Python function to check whether a number falls within a given range.
def check_range(number, start, end):
    return number in range(start, end + 1)


#2. Write a Python function to Print even numbers from 1 to 50
def print_even_numbers():
    for i in range(2, 51, 2):
        print(i)
# 3. Write a Python function to Sum of numbers from 1 to 100
def sum_numbers():
    return sum(range(1, 101))

#4. Print all numbers divisible by 5 between 1 and 100
def print_divisible_by_5():
    for i in range(5, 101, 5):
        print(i)

# 5.Create a list of numbers from 50 to 100 with a step of 5
def create_list_with_step():
    return list(range(50, 101, 5))

# 6. Print the square of each number from 1 to 10.
def print_squares():
    for i in range(1, 11):
        print(i * i)

# 7. Print numbers between -10 and 10.
def print_numbers_between():
    for i in range(-10, 11):
        print(i)
