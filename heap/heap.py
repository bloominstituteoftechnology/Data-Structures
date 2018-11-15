class Heap:
  def __init__(self):
    self.storage = []

# bubble the values from the end up to the start through the length of the array/list
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    value= self.storage[0]
    # first element replaced by last element
    self.storage[0]=self.storage[(len(self.storage)-1)]
    #delete last -pop off
    self.storage.pop()
    self._sift_down(0)
    return value

  def get_max(self):
   return self.storage[0]
# just the length of the array/list
  def get_size(self):
    return len(self.storage)
    

  def _bubble_up(self, index):
    # bubble up up up the heap
    # use the parent formula i-1//2 
    # swap values!!!
    # update the index
    while (index-1)//2>=0:
      if self.storage[(index-1)//2]<self.storage[index]:
        self.storage[index], self.storage[(index-1)//2] = self.storage[(index-1)//2], self.storage[index]
      index = ((index-1)//2)
    

  def _sift_down(self, index):
    pass
