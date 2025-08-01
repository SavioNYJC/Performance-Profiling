import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList():
    def  __init__(self):
        self.head = None
    
    def insert(self, node, index):
        if self.size == 0:
            self.head = node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
    
    def retrieve(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            else:
                current = current.next
                count += 1
        raise IndexError("Index out of range")

lst = LinkedList()
list10 = list(range(10))
list100 = list(range(100))
list1000 = list(range(1000))
list10000 = list(range(10000))

random.shuffle(list10)
random.shuffle(list100)
random.shuffle(list1000)
random.shuffle(list10000)

def test(size):
    shuffled_list = list(range(size))
    random.shuffle(shuffled_list)
    for i in range(len(shuffled_list)):
        lst.insert(shuffled_list[i])
    
    for i in range(len(shuffled_list)):
        lst.retrieve(i)

print('Time taken for 100 iterations of length 10: ', timeit.timeit(lambda: test(10), number=100))
print('Time taken for 100 iterations of length 100: ', timeit.timeit(lambda: test(100), number=100))
print('Time taken for 100 iterations of length 1000: ', timeit.timeit(lambda: test(1000), number=100))
print('Time taken for 100 iterations of length 10000: ', timeit.timeit(lambda: test(10000), number=100))
        
        