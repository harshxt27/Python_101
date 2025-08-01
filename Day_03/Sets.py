# Examples of Sets
# Creating a set
myset = {"apple", "banana", "cherry"}
print(myset)

# Accessing items in a set
for item in myset:
    print(item)

# Adding items to a set
myset.add("orange")
print(myset)

# Removing items from a set
myset.remove("banana")
print(myset)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))