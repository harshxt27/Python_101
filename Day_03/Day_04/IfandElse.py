#if condition:
#    # code to execute if condition is true
#    pass
# else:
#    # code to execute if condition is false

if 5 > 2:
    print("5 is greater than 2")

# Example of an if-else statement in Python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Example of an if-elif-else statement in Python
y = 20
if y > 30:
    print("y is greater than 30")
elif y > 20:
    print("y is greater than 20")
else:
    print("y is not greater than 30 or 20")

# Checking multiple conditions with logical operators
a = 15
if a > 10 and a < 20:
    print("a is between 10 and 20")
else:
    print("a is not between 10 and 20")

# Using the 'in' operator to check membership
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list of fruits")
else:
    print("Banana is not in the list of fruits")

# Using the 'not' operator to negate a condition
if not (x < 5):
    print("x is not less than 5")   
else:
    print("x is less than 5")
