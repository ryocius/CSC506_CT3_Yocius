import random
import time

# Selection Sort
# O(n^2)
def selectionsort(inArray):
    for i in range(len(inArray)):
        minIndex = i
        for j in range(i + 1, len(inArray)):
            if inArray[minIndex] > inArray[j]:
                minIndex = j

        inArray[i], inArray[minIndex] = inArray[minIndex], inArray[i]


# Iterative Insertion Sort
# O(n^2)
def insertionsort(inArray):
    for i in range(1, len(inArray)):
        key = inArray[i]

        j = i - 1
        while j >= 0 and key < inArray[j]:
            inArray[j + 1] = inArray[j]
            j -= 1

        inArray[j + 1] = key


# O(n) - Partition for Quick Sort
def partition(inArray, low, high):
    pivot = inArray[high]

    pointer = low - 1

    for i in range(low, high):
        if inArray[i] <= pivot:
            pointer += 1
            (inArray[pointer], inArray[i]) = (inArray[i], inArray[pointer])

    (inArray[pointer + 1], inArray[high]) = (inArray[high], inArray[pointer + 1])

    return pointer + 1

# Recursive Quick Sort
# O(n log(n))
def quicksort(inArray, low, high):
    if low < high:
        pivot = partition(inArray, low, high)

        quicksort(inArray, low, pivot - 1)

        quicksort(inArray, pivot + 1, high)


# Merge Sort
# O(n log(n))
def mergesort(inArray):
    if len(inArray) > 1:
        midpoint = len(inArray) // 2

        left = inArray[:midpoint]
        right = inArray[midpoint:]
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                inArray[k] = left[i]
                i += 1
            else:
                inArray[k] = right[j]
                j += 1
            k += 1

            while i < len(left):
                inArray[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                inArray[k] = right[j]
                j += 1
                k += 1


array1 = []
for i in range(500):
    array1.append(random.randint(0, 500))
array2 = array1
array3 = array1
array4 = array1
print(array1)
print(array2)
print(array3)
print(array4)


selectionsort(array1)
insertionsort(array2)
quicksort(array3, 0, len(array3)-1)
mergesort(array4)


print(array1)
print(array2)
print(array3)
print(array4)




start = time.perf_counter()

stop = time.perf_counter()
print(f"Recursive Quick Sort on a {len(array1)} item list takes {stop-start} seconds")


start = time.perf_counter()
insertionsort(array2)
stop = time.perf_counter()
print(f"Insertion Sort on a {len(array2)} item list takes {stop-start} seconds")




