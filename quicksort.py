import random
import timeit

unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67, 67]

def quick_sort(numlist):
    # Handle base case - length of array is 1
    if len(numlist) < 2:
        return numlist
    
    # Select last element of list as pivot (for convenience)
    pivot = numlist[-1]
    smallerElements = []
    largerElements = []
    del numlist[-1]

    # Split remaining list elements into greater-than and lesser-than
    # subarrays by comparing them with pivot
    for element in numlist:
        if element < pivot:
            smallerElements.append(element)
        elif element > pivot:
            largerElements.append(element)

    # Recursively sort greater and lesser-than subarrays and concatenate
    # them with the pivot
    
    return quick_sort(smallerElements) + [pivot] + quick_sort(largerElements)

def quick_sort_optimised(numlist):
    if len(numlist) < 2:
        return numlist
    
    # Choose a random number from the list as the pivot - improves efficienct
    # as the likelihood of the largest number being the last element of the 
    # list is greater, resulting in greater time complexity as one subarray 
    # will contain much more elements than the other subarray, increasing the
    # number of recursive calls that need to be made.
    
    pivot = numlist[random.randint(0,len(numlist) - 1)]
    smallerElements = []
    largerElements = []
    del numlist[-1]
    for element in numlist:
        if element < pivot:
            smallerElements.append(element)
        elif element > pivot:
            largerElements.append(element)
    
    return quick_sort(smallerElements) + [pivot] + quick_sort(largerElements)

    
# print(quick_sort(unsorted_list))
# print(quick_sort_optimised(unsorted_list))

list10 = list(range(10))
list100 = list(range(100))
list1000 = list(range(1000))
list10000 = list(range(10000))

random.shuffle(list10)
random.shuffle(list100)
random.shuffle(list1000)
random.shuffle(list10000)
    
print('Time taken for 100 iterations of length 10:', timeit.timeit(lambda: quick_sort_optimised(list10), number=100))
print('Time taken for 100 iterations of length 100:', timeit.timeit(lambda: quick_sort_optimised(list100), number=100))
print('Time taken for 100 iterations of length 1000:', timeit.timeit(lambda: quick_sort_optimised(list1000), number=100))
print('Time taken for 100 iterations of length 10000:', timeit.timeit(lambda: quick_sort_optimised(list10000), number=100))