# Sets do not allow duplicate elemets it contains only unique data
#unordered collection

# create a student_id set
stu_id = {112, 113, 114, 115, 115, 116, 8, 10,45}
print(stu_id)

# create a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
print(letters)

# create a mixed set
mixed_set = {"Hello", 1, -7, 8.9}
print(mixed_set)

# create an empty set
empty_set = set()

#add()
fruits = {"apple", "banana"}
fruits.add("orange")

print(fruits)

#clear()
s = {1,2,3}
s.clear()
print(s)

#copy()
a= {1,2,3}
b=a.copy()
print(b)

#difference()
a = {1,2,3,4}
b = {3,4,5}

c= a.difference(b)
print(c)

# diffrent update
a = {1,2,3,4}
b = {3,4}
a.difference_update(b)
print(a)

# discard()
s={1,2,3}
s.discard(2)
print(s)

#intersection
a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
print(c)

# intersection_update()
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)

# isdisjoint()
a = {1, 2}
b = {3, 4}
c=a.isdisjoint(b)
print(c)

# issubset()
a = {1, 2}
b = {1, 2, 3}
c = a.issubset(b)
print(c)

# issuperset()
a = {1, 2, 3}
b = {1, 2}
c = a.issuperset(b)
print(c)

# pop()
s = {1, 2, 3}
s.pop()
print(s)

# remove()
s = {1, 2, 3}
s.remove(2)
print(s)

# symmetric_difference()
a = {1, 2, 3}
b = {3, 4}
c = a.symmetric_difference(b)
print(c)

# symmetric_difference_update()
a = {1, 2, 3}
b = {3, 4}
a.symmetric_difference_update(b)
print(a)


# union()
a = {1, 2}
b = {3, 4}
c = a.union(b)
print(c)

# update()
a = {1, 2}
b = {3, 4}
a.update(b)
print(a)
