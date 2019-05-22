import time
from max_heap import Heap

def list_find_max_index(l):
  current_max = l[0]
  current_max_index = 0

  for i in range(0, len(l)):
    if l[i] > current_max:
      current_max = l[i]
      current_max_index = i

  return current_max_index

if __name__ == '__main__':
  n = 10000
  l = []
  h = Heap()

  # benchmark heap insertion vs list insertion

  # O(n) insertion for lists
  start_time = time.time()
  for i in range(0, n):
    l.append(i)
  end_time = time.time()
  print(f'list insertion runtime: {end_time - start_time} seconds')

  # O(n log n) insertion for heaps
  start_time = time.time()
  for i in range(0, n):
    h.insert(i)
  end_time = time.time()
  print(f'heap insertion runtime: {end_time - start_time} seconds')

#   # benchmark heap max value removal vs list max value removal
  
  # O(n log n) max removal for heaps
  start_time = time.time()
  for i in range(0, n):
    h.delete()
  end_time = time.time()
  print(f'heap remove max runtime: {end_time - start_time} seconds')

  # O(n^3) max removal for lists
  # O(n^2 + n^2)
  start_time = time.time()
  for i in range(0, n): # O(n)
    index = list_find_max_index(l) # O(n)
    l.pop(index) # O(n)
  end_time = time.time()
print(f'list remove max runtime: {end_time - start_time} seconds')