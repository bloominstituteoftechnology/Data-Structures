class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # add to last index
    self.storage.append(value)
    self.size += 1
    
    # bubble up the added value
    self._bubble_up(self.size)

  def delete(self):
    # switch top and last item
    self.swap(self.size, 0)
    
    # remove the last item
    delItem = self.storage.pop()
    self.size -= 1
    
    # sift down the top item
    self._sift_down(0)
    return delItem

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # find parent index
    pI = int(index/2)
    
    if self.storage[index] > self.storage[pI]:
      self.swap(pI, index)
      self._bubble_up(pI)

  def _sift_down(self, index):
    left = 2*index+1
    right = 2*index+2
    
    if left > self.size and right > self.size:
        return
    
    if right > self.size:
      self.swap(left, index)
      self._sift_down(left)
      return
    
    print("*********")
    print(left)
    print(right)
    print(self.size)
      
    # detect sift to left or right
    if self.storage[left] <= self.storage[right]:
        self.swap(right,index)
        self._sift_down(right)
    else:
        self.swap(left, index)
        self._sift_down(left)
  
  def swap(self, first, second):
    temp = self.storage[first]
    self.storage[first] = self.storage[second]
    self.storage[second] = temp