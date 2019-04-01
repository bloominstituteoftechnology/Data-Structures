import time
# is this okay
from linked_list import LinkedList

n = 100000

# initialize a list with 100000 integers
l = [i for i in range(n)]

# init a linked list with 100000 integers
ll = LinkedList()
for i in range(n):
    ll.add_to_tail(i)

start_time = time.time()

for i in range(n):
    ll.remove_from_head()
end_time = time.time()
print(f"linked list remove_from head runtime: {end_time - start_time}")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(
    f"list popping from the front runtime on 100000 integers: {end_time - start_time}")
