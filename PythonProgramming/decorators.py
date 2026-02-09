# Decorators - wrapper function around the function are called decorators

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def vanilla():
    print("I am the vanilla cake")

@make_pretty
def strawberry():
    print("I am the starberry cake")

vanilla()
strawberry()