import timeit
import random
unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def generate_shuffled_array(_range):
    array = list(range(_range))
    random.shuffle(array)
    return array


def bubble_sort_forloop(numlist):
    for i in range(len(numlist) - 1):
        for j in range(len(numlist) - 1):
            # Repeats sorting process n^2 times such that all elements are sorted
            if numlist[j] > numlist[j+1-i]:
                # Swap the positions of 2 adjacent elements if the first element is larger than the 
                # second element (assuming the list is being sorted in ascending order)
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp
    
    # print('iterations:', i)
    return numlist

def execute_10():
    array = generate_shuffled_array(10)
    bubble_sort_forloop(array.copy())
def execute_100():
    array = generate_shuffled_array(100)
    bubble_sort_forloop(array.copy())
def execute_1000():
    array = generate_shuffled_array(1000)
    bubble_sort_forloop(array.copy())
def execute_10000():
    array = generate_shuffled_array(10000)
    bubble_sort_forloop(array.copy())

print('time taken for 10 iterations: ' + str(timeit.timeit(execute_10, number=100)))
print('time taken for 100 iterations: ' + str(timeit.timeit(execute_100, number=100)))
print('time taken for 1000 iterations: ' + str(timeit.timeit(execute_1000, number=100)))
print('time taken for 10000 iterations: ' + str(timeit.timeit(execute_10000, number=100)))