from heap import Heap
from random import randint

def heap_sort(arr):
    arr_length = len(arr)
    s_heap = Heap()
    for i in range(0, arr_length):
        s_heap.insert(arr.pop())
    for i in range(0, arr_length):
        arr.append(s_heap.delete())
    arr.reverse()
    return arr

def create_arr(num = 10000, max_int = 10000):
    arr = []
    for i in range(0, num):
        arr.append(randint(0, max_int))
    return arr

test_arr = create_arr()
print('\nBEFORE: ')
print(test_arr)
print('\nAFTER: ')
print(heap_sort(test_arr))
