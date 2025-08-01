#example of a tuple in Python
# Tuples are immutable sequences in Python, typically used to store collections of heterogeneous data.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Accessing elements
print(mytuple[0])  # Output: apple
print(mytuple[1])  # Output: banana
print(mytuple[2])  # Output: cherry

# Attempting to change an element will raise an error
# mytuple[0] = "orange"  # Uncommenting this line will raise a TypeError

# Tuples can also contain different data types
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)

#tuple length
print(len(mytuple))  # Output: 3

# Tuple unpacking
a, b, c = mytuple
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry

# Nested tuples
nested_tuple = (mytuple, mixed_tuple)
print(nested_tuple)
# Output: (('apple', 'banana', 'cherry'), (1, 'hello', 3.14, True))

#tuple type
print(type(mytuple))  # Output: <class 'tuple'>
print(type(mixed_tuple))  # Output: <class 'tuple'>

