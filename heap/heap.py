class Heap:
  def __init__(self):
    self.storage = []

# bubble the values from the end up to the start through the length of the array/list
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    if self.get_size() > 1:
      removed_head = self.storage[0]
      self.storage[0] = self.storage.pop()
      self._sift_down(0)
    else:
      removed_head = self.storage.pop()
    return removed_head

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
    # left child formula : 2i+1
    # right child formula:2i+2
    # if 2i +2 <len(self.storage)
    while index*2 + 1 <= len(self.storage)-1:
      max_child=index*2+1
      if self.storage[index] < self.storage[max_child]:
         self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
      index=max_child

      
