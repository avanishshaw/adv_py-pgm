# Generators - special type of functions - return one value a time , on demand

# yeild -

# memery efficiency
# usefull large set of data
# files, retries, batching

# normal function

def numbers():
    return [1, 2, 3, 4,]

print(numbers())

# Generators

def generator():
    print("print 1")
    yield 1

    print("Print 2")
    yield 2

    print("Print 3")
    yield 3

    print("Print 4")
    yield 4

ret_val = generator()

print(next(ret_val))
print(next(ret_val))
print(next(ret_val))