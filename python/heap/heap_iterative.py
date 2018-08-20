# Title  : Max Heap using iterative approach
# Author : Frank Faustino
# Date   : 2018-08-18


class Heap:
  def __init__(self):
    self.storage = []

  def __len__(self):
    return len(self.storage)

  def _left(self, i):
    """Check if left child exists and return it."""
    return self.storage[(i * 2) + 1] \
      if (i * 2) + 1 < len(self) \
      else None

  def _right(self, i):
    """Check if right child exists and return it."""
    return self.storage[(i * 2) + 2] \
      if (i * 2) + 2 < len(self) \
      else None

  def _swap(self, a, b):
    tmp = self.storage[a]
    self.storage[a] = self.storage[b]
    self.storage[b] = tmp

  def insert(self, value):
    """Add value to the heap at the last index.
    Call _bubble_up to iteratively move the value towards
    the root index if it's larger than its parent.
    """
    self.storage.append(value)
    self._bubble_up(len(self) - 1)

  def delete(self):
    """Replace the value at the root index with the value at the last index,
    then remove the value at the last index from the array.
    Call _sift_down to iteratively move the value down towards
    the last index if it's smaller than either of its children.
    """
    tmp = self.storage[0]
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    self._sift_down(0)
    return tmp

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, i):
    """while loop's first condition prevents bubbling the root up.
    Also compares if the current value is greater than its parent's value.
    If both conditions are true perform a swap,
    then re-assign the value of i to the parent's index so
    the while loop continues at the parent index.
    Otherwise, we break the while loop.
    """
    while i > 0 and self.storage[i] > self.storage[i // 2]:
      self._swap(i, i // 2)
      i = i // 2

  def _sift_down(self, i):
    """while loop's condition prevents sifting down the last value of the heap.
    The first if statement:
      • Check that the current index has a right child.
      • Also check if that child's value is greater than its parent.
      • If both conditions are met, perform swap
    """
    while i < len(self):
      if self._right(i) and self.storage[i] < self._right(i):
        self._swap(i, (i * 2) + 2)
      elif self._left(i) and self.storage[i] < self.storage[i * 2 + 1]:
        self._swap(i, i * 2 + 1)
        i = i * 2 + 1
      else:
        break