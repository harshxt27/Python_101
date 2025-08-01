# Examples of Dictionaries
# Creating a dictionary
mydict = {"name": "Alice", "age": 25, "city": "New York"}
print(mydict)

# Accessing items in a dictionary
print(mydict["name"])
print(mydict.get("age"))

# Adding items to a dictionary
mydict["email"] = "alice@example.com"
print(mydict)

# Removing items from a dictionary
mydict.pop("city")
print(mydict)

# Dictionary methods
print(mydict.keys())
print(mydict.values())
print(mydict.items())

# Looping through a dictionary
for key, value in mydict.items():
    print(f"{key}: {value}")


# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}