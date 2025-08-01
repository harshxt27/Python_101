# Joining Tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange", "kiwi", "melon")
new_tuple = tuple1 + tuple2
print(new_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon')

# Joining tuples with different data types
tuple3 = (1, 2, 3)
tuple4 = ("hello", "world", 3.14, True)
new_tuple = tuple3 + tuple4
print(new_tuple)  # Output: (1, 2, 3, 'hello', 'world', 3.14, True)

#multiple tuples
tuple5 = ("red", "green")
tuple6 = ("blue", "yellow")
new_tuple = tuple5 + tuple6
print(new_tuple)  # Output: ('red', 'green', 'blue', 'yellow')