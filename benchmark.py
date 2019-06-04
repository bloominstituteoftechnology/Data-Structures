from time import time
from linked_list import LinkedList

"""
Cretate an array with 100,00 items
Time how long it takes to remove all of them 
from the front of a list and a linked list
respectively.
"""

n = 1000000
# a list contain n elements
l = [i for i in range(n)]

my_list = LinkedList()
# add n elements to the linked list
for i in range(n):
    my_list.add_to_tail(i)

start_time = time()
for _ in range(n):
    my_list.remove_head()

end_time = time()

ll_time = end_time - start_time
print(f'It took {ll_time} seconds to remove {n} from our linked list.')

start_time = time()
# remove n elements for the front of our array
for _ in range(n):
    l.pop(0)

end_time = time()
array_time = end_time - start_time
print(f'It took {array_time} seconds to remove {n} from our array.')