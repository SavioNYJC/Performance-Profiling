import timeit
import random

unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32]

def merge(left_array, right_array):
    sortingindex = 0
    sorted_array = []

    # Assumes left_array and right_array are already sorted
    while len(right_array) != 0 and len(left_array) != 0:
        # Compare first element of both arrays and add the smaller of the two
        # to a new array, repeating until one of the arrays no longer contains elements
        if left_array[0] > right_array[0]:
            sorted_array.append(right_array[0])
            del right_array[0]
        else:
            sorted_array.append(left_array[0])
            del left_array[0]

        sortingindex += 1
        # print(sorted_array)
    
    # Adds the remaining elements (if any) to the end of the sorted array, as 
    # these elements (assumed to also be sorted) are larger than all sorted elements 
    sorted_array += left_array
    sorted_array += right_array

    return sorted_array

def merge_sort(numlist):
    if len(numlist) < 2:
        # Handles base case - only 1 element to be sorted
        return numlist
    midindex = len(numlist) // 2
    # Sort the first half of the array
    first_half_array = merge_sort(numlist[0:midindex])
    # Sort the second half of the array
    second_half_array = merge_sort(numlist[midindex:])
    # Merge both arrays such that the combined elements are sorted in ascending order
    merged_array = merge(first_half_array, second_half_array)

    return merged_array

list10 = list(range(10))
list100 = list(range(100))
list1000 = list(range(1000))
list10000 = list(range(10000))

random.shuffle(list10)
random.shuffle(list100)
random.shuffle(list1000)
random.shuffle(list10000)
    
print('Time taken for 100 iterations of length 10:', timeit.timeit(lambda: merge_sort(list10), number=100))
print('Time taken for 100 iterations of length 100:', timeit.timeit(lambda: merge_sort(list100), number=100))
print('Time taken for 100 iterations of length 1000:', timeit.timeit(lambda: merge_sort(list1000), number=100))
print('Time taken for 100 iterations of length 10000: ', timeit.timeit(lambda: merge_sort(list10000), number=100))