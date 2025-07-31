#Listing all items in list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Iterating through a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for x in thislist:
  if x == "cherry":
    break
  print(x)  

#Using range to loop through a list
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using range and len to loop through a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a while loop to iterate through a list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1


#Using a while loop with a condition
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(thislist):
  if thislist[i] == "cherry":
    break
  print(thislist[i])
  i += 1


#Using a while loop with a condition and range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(thislist):
  if thislist[i] == "cherry":
    break
  print(thislist[i])
  i += 1


#Using a while loop with a condition and range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(thislist):
    if thislist[i] == "cherry":
        break
    print(thislist[i])
    i += 1