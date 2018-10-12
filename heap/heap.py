# class Heap:
#   def __init__(self):
#     self.heapArray = []
#
#   def insert(self, value):
#     pass
#
#   def delete(self):
#     pass
#
#   def get_max(self):
#     pass
#
#   def get_size(self):
#     pass
#
#   def _bubble_up(self, index):
#     pass
#
#   def _sift_down(self, index):
#     pass

class Heap:
  def __init__(self):
    self.heapArray = [0]
    self.size = 0

  def insert(self, value):
    self.heapArray.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    val_ue = self.heapArray[1]
    self.heapArray[1] = self.heapArray[self.size]
    self.size -= 1
    self.heapArray.pop()
    self._shift_down(1)
    return val_ue

  def get_max(self):
    return self.heapArray[1]
  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # bubbling the node at the giving index until it gets to a valid place
    # also loop until there is no valid parent index
    while index // 2 > 0:
      # checking if elements parent value is less than current value
      if self.heapArray[index // 2] < self.heapArray[index]:
        # Swap happens here
        self.heapArray[index // 2], self.heapArray[index] = self.heapArray[index], self.heapArray[index // 2]
      # Heap element found a good cosy place and stays here :D
      else:
        break
      # updating index value to become parent index in order to continue up the heap
      index = index // 2

  def _shift_down(self, index):
    # shifting down until element reaches a cosy place
    while (index * 2) <= self.size:
      # determine which child is higher value
      x = self._max_child(index)
      # check if x is the current node needs swapping
      if self.heapArray[index] < self.heapArray[x]:
        # if TRUE then swap
        self.heapArray[index], self.heapArray[x] = self.heapArray[x], self.heapArray[index]
      else:
        break
      index = x

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      # getting child with the highest value
      return index * 2 if self.heapArray[index * 2] > self.heapArray[index * 2 + 1] else index * 2 + 1
