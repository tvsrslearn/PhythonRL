from numpy import *

arr = array ([1,2,3,4,5,6,6], float)

print(arr)
print(arr.dtype)

linsArray = linspace(4, 20, 10)
print(linsArray)

a_rangeArray = arange(0, 30, 5)
print(a_rangeArray)

arr = a_rangeArray + 5
print("Printing added Array", arr)

arr2 = arr
print("arr2 = arr:. Here both are pointing to same address ", arr2)

print("Copy should be done using coy or array. This will make sure it is Deep Copy")
arr3 = arr2.copy()

print("Arra3:", arr3)

