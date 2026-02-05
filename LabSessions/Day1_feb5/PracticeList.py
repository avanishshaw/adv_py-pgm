numbers = [3, 8, 5, 12, 7, 9, 4]

# Write a Python program to get the largest number from a list.

largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]

print(largest)

# remove the even numbers from the lost
odd_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        odd_numbers.append(numbers[i])

print(odd_numbers)

#multiply the items in the list
product = 1

for i in range(len(numbers)):
    product = product * numbers[i]

print(product)