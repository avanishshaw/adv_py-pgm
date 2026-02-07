# Lists - data structure - Ordered Fashion - insertion order and allows duplicate values, mutable in nature stores set of test data - data types

empty_list = []
numbers = [1, 24,21,54,67,23,29]
mixed_data = [1, "hello", True, 6.67, 1]
nested = [[1, 2], [3, 4]]

#acessing the list elements (indexing concept)

print(mixed_data[1])
print(mixed_data[2])

# modifying the data
mixed_data[4] = 6
print(mixed_data)

# add elements
mixed_data.insert(5, 5)
print(mixed_data)

#append at the end
mixed_data.append("John")
print(mixed_data)

# remove the elements
mixed_data.remove("hello")
print(mixed_data)
mixed_data.pop()
print(mixed_data)


