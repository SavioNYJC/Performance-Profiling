import timeit
import random

unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def insertion_sort(numlist):

    for i in range(1,len(numlist)):
        target = numlist[i]
        sortedindex = i - 1
        # Keeps track of what index contains the last sorted element
        while sortedindex > 0 and numlist[sortedindex] > target:
            numlist[sortedindex + 1] = numlist[sortedindex]
            sortedindex -= 1
            # Determine insertion position of first unsorted element
        numlist[sortedindex + 1] = target
        # Insert element at its sorted position

    return numlist

list10 = list(range(10))
list100 = list(range(100))
list1000 = list(range(1000))
list10000 = list(range(10000))

random.shuffle(list10)
random.shuffle(list100)
random.shuffle(list1000)
random.shuffle(list10000)
    
print('Time taken for 100 iterations of length 10:', timeit.timeit(lambda: insertion_sort(list10), number=100))
print('Time taken for 100 iterations of length 100:', timeit.timeit(lambda: insertion_sort(list100), number=100))
print('Time taken for 100 iterations of length 1000:', timeit.timeit(lambda: insertion_sort(list1000), number=100))
print('Time taken for 100 iterations of length 10000:', timeit.timeit(lambda: insertion_sort(list10000), number=100))