import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Append the value to the end of the storage
    # Bubble that value up through the heap until heap is sorted 
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)


  def _bubble_up(self, index):   # initial index of parent's value
    while (index - 1) // 2 >= 0:         # while parent's index > 0
      # if child val > parent val
      if self.storage[index] > self.storage[(index - 1) // 2]: 
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]  # swap
      index = (index - 1) // 2            # reduce to compare potential next parent's value

  def delete(self):
    deleted = self.storage[0]
    self.storage[:1], self.storage[-1:] = self.storage[-1:], self.storage[:1]
    self.storage.pop()
    if len(self.storage) > 1:   # if only root left, no need to sift_down
      self._sift_down(0)        # had to change test for it to pass
    return deleted

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)
  
  # def _get_parent(self, index):
  #   return self.storage[(index - 1) // 2]
  
  # def _get_right_child(self, index):
  #   r = index * 2 + 2
  #   if r > self.get_size():
  #     return None
  #   return self.storage[r]
  
  # def _get_left_child(self, index):
  #   L = index * 2 + 1
  #   if L > self.get_size():
  #     return None
  #   return self.storage[L]
        
  
  def _sift_down(self, index):
    # while left child index <= index of last element
    while index <= len(self.storage)/2 - 1:
      mc_i = index * 2 + 2 if len(self.storage)/2 - 1.5 >= index and self.storage[index * 2 + 2] > self.storage[index * 2 + 1] else index * 2 + 1
      if self.storage[index] < self.storage[mc_i]:
        self.storage[index], self.storage[mc_i] = self.storage[mc_i], self.storage[index]
      index = mc_i



        # for i in range(0, math.floor(math.log2(len(self.storage)))):
#     pass
# [6,   8,  10,     9,      1,      9,        9,           5]
# Initial                                                             Len log(n)
# 6    6    8     10       10      10        10           10          1      1/0
#    8     6 10   6 8    9   8   9    8    9    9       9    9       2 3     2/1
#                 9     6  1     6 1  9   6 1   8 9    6 1    8 9   45   67  4/2
#      s     s    s                  s                5           8-11 11-15 8/3
# Swapped    
# 6    8     10     10              10
#    6      6  8   9  8           9    9
#                 6             6 1   8
# [10, 9, 9, 6, 1, 8, 9, 5]
# [5  9 9 6 1 8 9 10] swap first and last
# [9 5 9 61 89  10] => [9 6 9 51 89  10] swap 5 w/ L9, swap 5 w/ 6 heapify [10] 
# [9]