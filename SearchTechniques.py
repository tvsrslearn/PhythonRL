from array import *
from SortTechniques import *

def LinearSearch(numberToSearch, arrayList):

    print("Linear Search")
    for i in range(len(arrayList)):
        if arrayList[i] == numberToSearch:
            print(i+1)
            return i

def BinarySearch(numberToSearch, arrayList):
    print("Sorting the array and then performing Binary Search")
    SelectionSort(arrayList)

    start = 0
    end = len(arrayList)-1
    mid = int((start + end)/2)
    while 1:
        if arrayList[mid] == numberToSearch:
            print(mid)
            return mid

        if arrayList[mid] < numberToSearch:
            start = mid + 1

        if arrayList[mid] > numberToSearch:
            end = mid - 1;

        mid = int((start + end)/2)


arrayElements = array('i', [10, 5, 7, 9, 12, 18, 4, 3, 5, 7, 1])

arrayListG = [10, 5, 7, 9, 12, 18, 4, 3, 5, 7, 1]
print(arrayElements)
print(arrayListG)
nToSearch = int(input("Enter Number to Search"))

LinearSearch(nToSearch, arrayListG)
BinarySearch(nToSearch, arrayListG)