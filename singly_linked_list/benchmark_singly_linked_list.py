import time
from singly_linked_list import LinkedList, Node

n = 1000000

l = []
ll = LinkedList()

start_time = time.time()
for i in range(n):
    l.append(i)
end_time = time.time()
print(f'Adding {n} elements to the list took {end_time - start_time} seconds')

start_time = time.time()
for i in range(n):
    ll.add_to_tail(n)
end_time = time.time()
print(f'Adding {n} elements to the linked list took {end_time - start_time} seconds')


start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f'List pop from front took {end_time - start_time} seconds')


start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f'Linked list pop from front took {end_time - start_time} seconds')