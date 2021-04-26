# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from array import *
from numpy import *

x=int(input("Enter Number of Rows to Print"))
y=int(input("Enter Number of Columns to Print"))
for i in range(x):
    for j in range(x-i):
        print("# ", end="")
    # Printing to make sure it goes to next line
    print()

vals = array('i', [10, 5, 9, 4, 2])
print(vals)
print(vals.buffer_info())
for va in vals:
    print(va)

print("Printing New Array")

newArray = array(vals.typecode, (a for a in vals))
newArray.reverse()
for newV in newArray:
    print(newV)

print("Dynamic Numbers from User")
dynArrFromUser = array('i', [])
n = int(input("Enter the Length of the Array"))
for i in range(n):
    x = int(input("Enter the Next Element"))
    dynArrFromUser.append(x)

print(dynArrFromUser)

valueToSearch = int(input("Enter the Value to Search"))
k = 0
for elem in dynArrFromUser:
    if(elem == valueToSearch)
        print("Index of the string is: ", k)
        break
    k+=1
else:
    print("Value not available in inputArray")


