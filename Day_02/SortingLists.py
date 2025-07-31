#sorting alphabetically
thislist = ["banana", "cherry", "apple"]
thislist.sort()
print(thislist)

#sorting in reverse order
thislist = ["banana", "cherry", "apple"]
thislist.sort(reverse=True)
print(thislist)

#sorting numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sorting numerically in reverse order   
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

#sorting case-insensitive
thislist = ["banana", "Cherry", "apple"]
thislist.sort(key=str.lower)
print(thislist)

#sorting case-insensitive in reverse order
thislist = ["banana", "Cherry", "apple"]
thislist.sort(key=str.lower, reverse=True)
print(thislist)

#Customized sorting with a function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

