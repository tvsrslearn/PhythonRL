def TriangleOutput(n):
    for i in range(n):
        print(' '*(n-i+1), '*'*(2*i+1))


def CheckPalindrome(num):
    reversedNum = num[::-1]
    if reversedNum == num:
        print("Yes, Given Number is a palindrome")
    else:
        print("Given number is not a palindrome")

num = int(input("Enter the number for desired output "))
TriangleOutput(num)


A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)

