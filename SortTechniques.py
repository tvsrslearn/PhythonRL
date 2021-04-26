

#Bubble Sort: This is done by comparing and swapping the adjacent numbers till end.
#             By the end of firt iteration at the end of inner loop, greatest number will be at the end
#             Then again start from first till end-1 position

def bubbleSortC(numsForSort):

    for i in range(len(numsForSort)-1, 0, -1):   #range(start, end, -1)  -1 is for reverse
        for j in range(i):
            if numsForSort[j] > numsForSort[j+1]:
                numsForSort[j], numsForSort[j+1] = numsForSort[j+1], numsForSort[j]

        print(numsForSort) # Just to see whats the oreder of nums after each iteration


# Selection Sort: In Selection we do a lot of swapping and its costly
#                 Here in selection sort, we first get the least/greatest number position and exhange
#                 the value from that position to the first. Here we will know where it is sorted. i.e. i [Outerloop]
#                 Remember the position till where it is sorted. Find the minimum from minThis is done by comparing and swapping the adjacent numbers till end.
#                 Its just like find the mimium vale. swap it with first position. then next and next till end.
def SelectionSort(numsForSort):
    for i in range(len(numsForSort)):
        minpos = i
        for j in range(i, len(numsForSort)):
            if numsForSort[minpos] > numsForSort[j]:
                minpos = j
        numsForSort[i], numsForSort[minpos] = numsForSort[minpos], numsForSort[i]

        print(numsForSort)  # Just to see whats the oreder of nums after each iteration


#Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
#The array is virtually split into a sorted and an unsorted part.
#Values from the unsorted part are picked and placed at the correct position in the sorted part.
#Algorithm
#To sort an array of size n in ascending order:
#1: Iterate from arr[1] to arr[n] over the array.
#2: Compare the current element (key) to its predecessor.
#3: If the key element is smaller than its predecessor, compare it to the elements before.
#   Move the greater elements one position up to make space for the swapped element.
# Insertion sort is used when number of elements is small.
#    It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
def InsertionSort(numsForSort):
    for i in range(1, len(numsForSort)):
        temp = numsForSort[i]
        currentPos = i
        while currentPos != 0 and numsForSort[currentPos-1] > temp:
                numsForSort[currentPos] = numsForSort[currentPos-1]
                currentPos = currentPos - 1

        numsForSort[currentPos] = temp
        print(numsForSort)

def MergeSort(numsForSort):

    if len(numsForSort) <= 1:
        return

    mid = int(len(numsForSort)/2)

    leftSplitArray = numsForSort[:mid]
    rightSplitArray = numsForSort[mid:]

    MergeSort(leftSplitArray)
    MergeSort(rightSplitArray)

    i=j=k=0

    #Merging of left and right array till one of the loop is completely copied into formal argument recieved
    while i < len(leftSplitArray) and j < len(rightSplitArray):
        if leftSplitArray[i] < rightSplitArray[j]:
            numsForSort[k] = leftSplitArray[i]
            i = i + 1
        else:
            numsForSort[k] = rightSplitArray[j]
            j = j + 1

        k = k +1

    # this is for copying the rest of the elements in left array
    # if right side array is copied into array that is passed as argument
    while i < len(leftSplitArray):
        numsForSort[k] = leftSplitArray[i]
        i = i + 1
        k = k + 1

    # this is for copying the rest of the elements in right array
    # if left side array is copied into array that is passed as argument
    while j < len(rightSplitArray):
        numsForSort[k] = rightSplitArray[j]
        j = j + 1
        k = k + 1


nums = [4, 5, 9 , 4, 1, 7, 2]
#SelectionSort(nums)
#InsertionSort(nums)
MergeSort(nums)


print(nums)