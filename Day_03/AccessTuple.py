#range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#check if an item exists
if "banana" in thistuple:
    print("Yes, 'banana' is in the tuple")  

# Accessing elements in a tuple
print(thistuple[1])  # Output: banana

#change tuple value
# Tuples are immutable, so we cannot change their values
# However, we can create a new tuple with the desired changes
new_tuple = thistuple[:1] + ("blueberry",) + thistuple[2:]
print(new_tuple)  # Output: ('apple', 'blueberry', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

#add items to a tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
new_tuple = thistuple + ("blueberry",)
print(new_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'blueberry')

#remove items from a tuple
new_tuple = thistuple[:2] + thistuple[3:]
print(new_tuple)  # Output: ('apple', 'banana', 'orange', 'kiwi', 'melon', 'mango')
# Output: (('apple', 'banana', 'cherry'), (1, 'hello', 3.14, True))
# Output: <class 'tuple'>

