import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    max_num = self.get_max()
    self.storage[0] = self.storage[-1]
    del self.storage[-1]
    self._sift_down(0)
    return max_num

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    p_index = math.floor((index - 1)/2)
    if index > 0 and self.storage[p_index] < self.storage[index]:
      temp = self.storage[p_index]
      self.storage[p_index] = self.storage[index]
      self.storage[index] = temp
      self._bubble_up(p_index)


  def _sift_down(self, index):
    print(f"index: {index}")
    print(f"max_index: {len(self.storage) -1}")
    if len(self.storage) <= 1:
      return

    print((index*2 + 1))
    if (index*2 + 1) >= len(self.storage) - 1:
      return




    # check left
    # a,b = b,a means to swap
    # check order
    left = self.storage[index * 2 + 1]
    right = self.storage[index * 2 + 2]

    if not right:
      larger_index = (index * 2 + 1)
      # means that the heap is ordered properly
      if self.storage[index] > left:
        return
    elif left >= right:
      larger_index = (index * 2 + 1)
    else:
      larger_index = (index * 2 + 2) 

    # indicates that the list is ordered properly
    if self.storage[index] > self.storage[larger_index]:
      return
    print(larger_index)
    self.storage[index], self.storage[larger_index] = self.storage[larger_index], self.storage[index]
    self._sift_down(larger_index)


    print(larger_index)
    

print(math.floor(7/5))

heap = Heap()
heap.storage = [100,22,33,44,56,29]
heap.delete()
print(heap.storage)
