#Boolean values
print(True)
print(False)

#Boolean expressions
print(10 > 9)
print(10 < 9)
print(10 == 10)
print(10 != 9)

#Boolean expressions with strings
print("apple" == "apple")
print("apple" != "banana")      

#Boolean expressions with lists
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] != [1, 2, 4])

#Boolean expressions with mixed types
print(10 == "10")  # False, different types
print(10 == 10.0)  # True, same value, different types

#Boolean expressions with None
print(None == None)  # True, both are None
print(None != None)  # False, both are None

#Boolean expressions with logical operators
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

#Boolean expressions with lists and logical operators
print([1, 2] and [3, 4])  # Returns the second
print([1, 2] or [3, 4])   # Returns the first

#Boolean expressions with conditions
age = 20
print(age >= 18)  # True, age is greater than or equal to 18
