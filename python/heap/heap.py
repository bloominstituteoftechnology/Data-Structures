# Title  : Max Heap using recursive approach
# Author : Frank Faustino
# Date   : 2018-08-18


class Heap:
  def __init__(self):
    self.storage = []

  def __len__(self):
    return len(self.storage)

  def _swap(self, x, y):
    a = self.storage[x]
    b = self.storage[y]
    self.storage[y] = a
    self.storage[x] = b

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self) - 1)

  def delete(self):
    tmp = self.storage[0]
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    print(f'deleted: {tmp}')
    self._sift_down(0)
    return tmp

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, i):
    if i > 0 and self.storage[i] > self.storage[i // 2]:
      self._swap(i, i // 2)
      self._bubble_up(i // 2)

  def _sift_down(self, i):
    left = (2 * i) + 1
    right = (2 * i) + 2
    largest = i
    if right < len(self) and self.storage[right] > self.storage[largest]:
        largest = right
    if left < len(self) and self.storage[left] > self.storage[largest]:
        largest = left
    if largest != i:
        self._swap(i, largest)
        self._sift_down(largest)
