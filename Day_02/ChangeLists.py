#Accessing elements in a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Changing elements in a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Adding elements to a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Inserting elements in a list
thislist = ["apple", "banana", "cherry"]    
thislist.insert(1, "orange")
print(thislist)

#Removing elements from a list
thislist = ["apple", "banana", "cherry"]    
thislist.remove("banana")
print(thislist)

#Removing elements by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Removing the last element
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Clearing a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

