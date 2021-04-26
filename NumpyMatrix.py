from numpy import *
from array import *

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact

num = int(input("Enter the number whose factorial is needed"))
print(num)
print("Factorial of ", num, "is:", factorial(num))

a=array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)
a.extend([4.5,6.3,6.8])
print(a)
a.insert(2,3.8)
print(a)