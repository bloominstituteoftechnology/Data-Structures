class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)
          
         
         

  
  def delete(self):
    val_ue = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return val_ue

  def get_max(self):
    return self.storage[1]
  
  def get_size(self):
     return self.size

 

  def _bubble_up(self, index):
    # index is the index of the element that will be moving up the heap
    # keep bubbling the element at the given index up the heap until it reaches a valid spot
    while index // 2 > 0:
      # check to see if the element's parent value is less than the current value
      if self.storage[index // 2] < self.storage[index]:
        # swap the values
        self.storage[index], self.storage[index // 2] = self.storage[index // 2],self.storage[index]
      # update the index to be the parent's index so that can continue moving up
      else:
        break
      index = (index) // 2



  def _sift_down(self, index):
     # shifting down until element reaches a cosy place
    while (index * 2) <= self.size:
      # determine which child is higher value
      x = self._max_child(index)
      # check if x is the current node needs swapping
      if self.storage[index] < self.storage[x]:
        # if TRUE then swap
        self.storage[index], self.storage[x] = self.storage[x], self.storage[index]
      else:
        break
      index = x

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
        # getting child with the highest value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1
         