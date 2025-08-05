# Lambda Functions

# Example 1: Simple lambda function
square = lambda x: x ** 2
print("The square of 5 is: " + str(square(5)))

# Example 2: Lambda function with multiple arguments
add = lambda a, b: a + b
print("The sum of 3 and 4 is: " + str(add(3, 4)))

# Example 3: Lambda function as an argument
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("The squared numbers are: " + str(squared_numbers))

# Example 4: Lambda function with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("The even numbers are: " + str(even_numbers))
