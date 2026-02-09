# exceptions - runtime errors which will disrupt the normal program flow
#Benefits - 1. Helps in debugging 2. Prevents program crashing 3. Handling errors and exception in the code more efficiently

# try-except

# try - code to be executed
# except - exception details catching
# else : if the exception does not occur then else part will be executed
# finally - mandate code
# custom exception

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")

try:
    a = 10/2
except Exception as e:
    print(e)
#runs only if no exception occurs
else:
    print("Division Successfully")
# mandatory code
finally:
    print("Close the browser")


#custom exception - creating a own exception
age = int(input("Enter the age"))
if age < 18:
    raise ValueError("Age must be 18 or above")
