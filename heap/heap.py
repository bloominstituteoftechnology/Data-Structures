import math
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage)-1
    if len(self.storage) >= 2:
      self._bubble_up(index)

  def delete(self):
    size = len(self.storage)
    top = self.storage[0]
    self.storage[0] = self.storage[size-1] 
    self._sift_down(0)
    return top

  def get_max(self):
    if len(self.storage) > 0:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
   
    while (index -1) // 2 >= 0:
      if self.storage[(index -1) // 2] < self.storage[index]:
        self.storage[(index -1) // 2], self.storage[index] = self.storage[index], self.storage[(index -1) // 2]
      index = (index -1) // 2


  def _sift_down(self, index):
    while (index*2 + 1) < len(self.storage):
      if self.storage[index*2+2]:
        left_child = self.storage[index*2+1]
        right_child = self.storage[index*2+2]
        if left_child > right_child:
          if left_child > self.storage[index]:
            #swap(left, parent)
            self.storage[index*2+1], self.storage[index] = self.storage[index], self.storage[index*2+1]
            #set index to left
            index = index*2+1
        else:
           if right_child > self.storage[index]:
             #swap(right, parent)
             self.storage[index*2+2], self.storage[index] = self.storage[index], self.storage[index*2+2]
             #set index to right
            index = index*2+2

    # left_child_index = self._get_left_child_index(index)
    # right_child_index = self._get_right_child_index(index)
    
    # if left_child_index:
    #   if self.storage[left_child_index] > self.storage[right_child_index]:
    #     self._swap(left_child_index, index)
    #   else:
    #     self._swap(right_child_index, index)

  def _get_parent_index(self, index):
    return math.floor((index - 1) / 2)

  def _get_left_child_index(self, index):
    return (index * 2) + 1

  def _get_right_child_index(self, index):
    return (index * 2) + 2
  
  def _swap(self, index, parent_index):
    tmp = self.storage[index]
    self.storage[index] = self.storage[parent_index]
    self.storage[parent_index] = tmp



# heap = Heap()
# heap.insert(6)
# heap.insert(8)
# heap.insert(10)