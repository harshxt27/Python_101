## Looping through a tuple
thistuple = ("apple", "banana", "cherry")
for item in thistuple:
    print(item)


#loop through tuple with index
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

