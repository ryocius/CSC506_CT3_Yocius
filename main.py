import random
import timeit
import math


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


def proveTheyWork():
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
    quicksort(array3, 0, len(array3) - 1)
    mergesort(array4)

    print("Selection Sorted")
    print(array1)
    print("Insertion Sorted")
    print(array2)
    print("Quick Sorted")
    print(array3)
    print("Merge Sorted")
    print(array4)


# Benchmark analysis function, takes a code snippet in
def benchmarkAnalysis(IN_CODE):
    SETUP_CODE = '''
import random
from __main__ import insertionsort, selectionsort, quicksort, mergesort
'''

    TEST_CODE = '''
array1 = []
for i in range(500):
    array1.append(random.randint(0, 500))
    '''

    TEST_CODE = TEST_CODE + IN_CODE

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=100)
    return min(times)


# Main function, sets up the various code run by each benchmark, executes, and prints
def main():
    SELECTION_CODE = '''
selectionsort(array1)
'''

    INSERTION_CODE = '''
insertionsort(array1)
'''

    QUICK_CODE = '''
quicksort(array1, 0, len(array1) - 1)
'''

    MERGE_CODE = '''
mergesort(array1)
'''

    proveTheyWork()

    print(
        f"Selection Sort: Time for the best 100 iterations out of 3 runs is {round(benchmarkAnalysis(SELECTION_CODE), 4)} seconds")
    print(
        f"Insertion Sort: Time for the best 100 iterations out of 3 runs is {round(benchmarkAnalysis(INSERTION_CODE), 4)} seconds")
    print(
        f"Quick Sort: Time for the best 100 iterations out of 3 runs is {round(benchmarkAnalysis(QUICK_CODE), 4)} seconds")
    print(
        f"Merge Sort: Time for the best 100 iterations out of 3 runs is {round(benchmarkAnalysis(MERGE_CODE), 4)} seconds")


main()
