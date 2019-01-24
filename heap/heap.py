import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    deleted = []
    print(self.storage)
    [self.storage[0]], self.storage[-1:] = self.storage[-1:], [self.storage[0]]
    # print(self.storage)

    deleted = [self.storage.pop()] + deleted
    print(self.storage)
    self._sift_down(0)  

    print(self.storage, deleted)
    

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    p_idx = (index - 1) // 2              # initial index of parent's value
    while p_idx >= 0:                     # while parent's index > 0
      if self.storage[index] > self.storage[p_idx]: # if child val > parent val
        self.storage[index], self.storage[p_idx]                                = self.storage[p_idx], self.storage[index]  # swap
      p_idx -= 2             # reduce to compare potential next parent's value

  def _sift_down(self, index):    # index 0
    for i in range(0, int(math.log2(math.floor(len(self.storage))))):
      # print(int(math.log2(math.floor(len(self.storage))))+1)
      print(self.storage, 's')
      if self.storage[index] < self.storage[(index * 2) + 1]:

        self.storage[index], self.storage[(index * 2) + 1] = self.storage[(index * 2) + 1], self.storage[index]
        # print(self.storage, 'if')
        index = (index * 2) + 1
      elif self.storage[index] > self.storage[(index * 2) + 2]:
        self.storage[index], self.storage[(index * 2) + 2] = self.storage[(index * 2) + 2], self.storage[index]
        index = (index * 2) + 2
        # print(self.storage, 'elif')
    print(self.storage, 'sifted')                                                        # log2(idx+1) = 3
    pass
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
# [9 5 9 61 89  10] => [9 6 9 51 89  10] swap 5 with L9, swap 5 with 6 heapify 