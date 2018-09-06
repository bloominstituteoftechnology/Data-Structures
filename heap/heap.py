class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value) #inserts value
    self.size += 1 #increases size of heap by 1
    self._bubble_up(len(self.storage) - 1) # calls bubble up function to adjust the location of the value based on parent index

  def delete(self):    
    first = self.storage.pop(0) 
    self.size -= 1
    self.storage = self.storage[-1:] + self.storage[:-1]
    self._sift_down(0)
    return first

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index): #keep looping up until it reaches the proper parent index
    node_index = index
    while node_index > 0:
        parent_index = (node_index-1)//2
        if self.storage[node_index] <= self.storage[parent_index]:
            break
        self.storage[node_index], self.storage[parent_index] = self.storage[parent_index], self.storage[node_index]
        node_index = parent_index

  def _sift_down(self, index):
   
    leftchild = index * 2 + 1
    rightchild = index * 2 + 2
    newindex = index

      
    if leftchild <= self.size -1:
      left_child_val = self.storage[leftchild]
      if left_child_val > self.storage[newindex]:
        newindex = leftchild
    if rightchild <= self.size -1:
      right_child_val = self.storage[rightchild]
      if right_child_val > self.storage[newindex]:
        newindex = rightchild
    if newindex is not index:
      self.storage[index], self.storage[newindex] = self.storage[newindex], self.storage[index]
      self._sift_down(newindex)