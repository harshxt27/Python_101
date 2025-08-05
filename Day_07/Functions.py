# Functions

def greet(name):
    print("Hello, " + name + "!")

def add_numbers(a, b):
    return a + b

# Example 1: Call greet function
greet("Alice")

# Example 2: Call add_numbers function
result = add_numbers(5, 10)
print("The sum is: " + str(result))

# Example 3: Function with default parameter
def multiply(a, b=2):
    return a * b

# Example 3: Call multiply function with default parameter
result_default = multiply(5)
print("The product is: " + str(result_default))

