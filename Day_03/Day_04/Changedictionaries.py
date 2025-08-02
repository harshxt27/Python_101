#change dictionaries in Python
# Dictionaries are mutable mappings in Python, used to store key-value pairs.
mydict = {"name": "Alice", "age": 30, "city": "New York"}
print(mydict)

# Accessing values by key
print(mydict["name"])  # Output: Alice
print(mydict["age"])   # Output: 30
print(mydict["city"])  # Output: New York
# Changing a value
mydict["age"] = 31
print(mydict["age"])   # Output: 31
# Adding a new key-value pair
mydict["country"] = "USA"
print(mydict["country"])  # Output: USA

