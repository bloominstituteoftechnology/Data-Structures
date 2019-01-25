class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    index = self.size - 1
    self._bubble_up(index)
    #if empty just insert item
    # if len(self.storage) == 0:
    #   self.storage.append(value)
    #   self.count += 1
    #   parent = _get_parent(self.count -1) #off by one??? maybe?
    #   while parent < value: 
    #     self._bubble_up(self.count -1)
    #     parent = _get_parent(self.count -1) #off by one??? maybe not -1?
        
    #otherwise insert item to end and sift it up


  def delete(self):
    val = self.storage[0]
    self.size += 1
    index = self.size - 1
    self.storage[0] = self.storage[length]
    self.storage.pop()
    self._sift_down(0)
    return val

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

#underscore means private function for internal use only
#   def _get_parent(self, index):
#     return storage[(index-1)//2]

#   def _get_left(self, index):
#     left_index = index*2+1
#     if left_index > len(self.storage) - 1:
#       return None
#     else: 
#       return left_index

#  def _get_right(self, index):
#     right_index = index*2+2
#     if left_index > len(self.storage) - 1:
#       return None
#     else: 
#       return right_index

  

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index - 1) // 2]
      index = (index - 1) // 2


  def _sift_down(self, index):
    pass
