class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # 1. Check last 
    self[len(self)] = v
    # 2. Find Index of last value
    index = self.length-1
    # 3.
    while (i > 1 and self[parent(i)] < self(i))
        (self[i], self[parent(i)])


  def delete(self):
    # 1. Find 
    parent = (len(self) -1) // 2
    # 2. Remove parent
    # 3. Replace parent position.

  def get_max(self):
    max = (len(self) -1) // 2
    return max

  def get_size(self):
    size = len(self) + 1
    return size

  def _bubble_up(self, index):
    pass

  #For Max Heap
  def _sift_down(self, index):
    parent_index = index
    left = parent_index * 2 +1
    right = parent_index * 2 * 
    
    maxIndex = left if self.storage[left] > self.storage[right] else 
    
    while self.storage[parent_index] < self.storage[maxIndex]:
    
    #swap parent & max 
        temp = self.storage[parent_index]
        self.storage[parent_index] = self.storage[maxIndex]
        self.storage[maxIndex] = temp
    #update index to be max_child's index
        parent_index = maxIndex
        left = parent_index * 2 +1
        right = parent_index * 2 +2

        maxIndex = left if self.storage[left] > self.storage[right] else right
