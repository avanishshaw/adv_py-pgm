# a = range(5)
# print(a[1])
# print(a[2])
# a1 = range(2, 5)
# print(a1[1])
#
# a1 = range(2,5)
# print(a1[1])
#
# a = range(2, 5)
# for i in a:
#     print(i)
#
#
# a = range(15, 2, -1)
#
# for i in a:
#     print(i)
#
# for attempt in range(3):
#     pin = input("Enter the pin: ")
#     if pin == "1234":
#         print("Access granted")
#         break
#     else:
#         print("Account locked")
#
# prices = [100, 200, 300, 400]
#
# for i in range(len(prices)):
#     if i % 2 == 0:
#         print("Discount applied on item {i}")
#
#
# #Scenario : Simulate polling every second for 10 second
#
# import time
#
# for second in range(10):
#     print("Checking the status at {second} sec")
#     time.sleep(1)

# accessing of the enumerate values

a = ['God', 'is', 'Great']
b = enumerate(a)
nxt_val = next(b)
print(nxt_val)
