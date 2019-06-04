import time
import random
from binary_search_tree import BinarySearchTree

"""
Computes the average time it takes to check containment
of a random value in a list over n_runs
"""
def list_bench(l, n, n_runs):
  total_time = 0
   
  for _ in range(0, n_runs):
    random_num = random.randint(0, n-1)

    start_time = time.time()
    random_num in l
    end_time = time.time()

    total_time += end_time - start_time

  return total_time / n_runs

"""
Computes the average time it takes to check containment
of a random value in a BST over n_runs
"""
def bst_bench(b, n, n_runs):
  total_time = 0

  for _ in range(0, n_runs):
    random_num = random.randint(0, n-1)

    start_time = time.time()
    b.contains(random_num)
    end_time = time.time()

    total_time += end_time - start_time

  return total_time / n_runs

"""
Benchmarking BST contains method over 500 runs in comparison 
with checking membership in a list over the same number of runs
"""
if __name__ == '__main__':
  n = 1000000
  random.seed()

  l = [i for i in range(0, n)]
  # shuffle the list
  random.shuffle(l)

  b = BinarySearchTree(n // 2)

  for i in range(0, n):
    b.insert(l[i])

  print(f'list contains average runtime: {list_bench(l, n, 500)} seconds') 
print(f'BST contains average runtime: {bst_bench(b, n, 500)} seconds')