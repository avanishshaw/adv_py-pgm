# 1.1.Handle FileNotFoundError Exception When Opening a File

try:
    with open("Data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

# 2.write a program to handle invalid user input

try:
    a = int(input("Enter a number: "))
    print("you entered:", a)
except ValueError:
    print("Invalid Input")


# 3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
import string

#random alphabet
char = random.choice(string.ascii_letters)
print("Random alphabetical character:", char)

# random alphabetical string
length = random.randint(1, 10)
random_string = ""
for i in range(length):
    random_string += random.choice(string.ascii_letters)

print(random_string)

#random alphabetical string of fixed length
length = int(input("Enter number of char you wanr in string: "))
fixed_string = ""

for i in range(length):
    fixed_string += random.choice(string.ascii_letters)

print(fixed_string)