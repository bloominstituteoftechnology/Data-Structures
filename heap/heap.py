class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0
  def insert(self, value):
      self.size += 1
      self.storage.append(value)
      self._bubble_up(self.size-1)
    
  def delete(self):
    self.size -= 1
    removed = self.storage[0]
    popped = self.storage.pop()
    if self.size > 0:
       self.storage[0] = popped
       self._sift_down(0) # should always been the 0 index no variable needed.
    return removed

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):

    while (index-1)//2 >= 0:
  
      if self.storage[(index-1)//2] < self.storage[index]:
        self.storage[index], self.storage[(index-1)//2] = self.storage[(index-1)//2], self.storage[index]
      index = (index-1)//2

  

  def _sift_down(self, index):

    # while ((2 * index) + 1) < self.size -1:
    #   left_child_idx = (2*index) + 1
    #   right_child_idx = (2*index) + 2
    #   if self.storage[left_child_idx] >= self.storage[right_child_idx]:
    #     if self.storage[left_child_idx] > self.storage[index]:
    #       self.storage[index], self.storage[left_child_idx] = self.storage[left_child_idx], self.storage[index]
    #   else:
    #     if self.storage[right_child_idx] > self.storage[index]:
    #       self.storage[index], self.storage[right_child_idx] = self.storage[right_child_idx], self.storage[index]
    #   index = (2*index) + 1 # base case
    # self._bubble_up(index)
    while ((2*index) + 1) < self.size-1:
        if self.storage[((2*index) + 1)] >= self.storage[((2*index) + 2)]:
            if self.storage[(2*index) + 1] > self.storage[index]: 
                self.storage[(2*index) + 1], self.storage[index] = self.storage[index], self.storage[(2*index) + 1]
                #destructuring assignment 
        else:
            if self.storage[(2*index) + 2] > self.storage[index]:
                self.storage[(2*index) + 2], self.storage[index] = self.storage[index], self.storage[(2*index) + 2]
                #destructuring assignment 
        index = (2*index)+ 1
    self._bubble_up(index)
    return True

    

  

     