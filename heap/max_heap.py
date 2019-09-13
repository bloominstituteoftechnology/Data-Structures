class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value) #insert in the left most postion of the tree
    val_index = len(self.storage) - 1
    self._bubble_up(val_index)

  def delete(self):
    max_value = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()

    self._sift_down(0)
    return max_value
  #store what is at back in the front
  #put the smallest value at the front, then remove it from our storage
  #call shift_down
  #return value
  
  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1 ) // 2
      if self.storage[index] > self.storage[parent]:
          self.storage[index] , self.storage[parent] = self.storage[parent] , self.storage[index]
          index = parent #updating your new index
      else:
          break

  def _sift_down(self, index):
    max_index = len(self.storage) - 1
    child_index = (2 * index) + 1

    while child_index <= max_index:
      right_child_index = child_index + 1
      if right_child_index <= max_index and self.storage[right_child_index] > self.storage[child_index]:
        child_index = right_child_index

      if self.storage[child_index] > self.storage[index]:
        self.storage[child_index], self.storage[index] = self.storage[index], self.storage[child_index]
        index = child_index
        child_index = (2 * index) + 1
      
      else:
        break
  #while index is less than max index
  #look at both children, choose the biggest
  #left child 2 * index + 1
  #right child 2 * index + 2
  #swap with that child,if the chosen one is larger update the index to the new location
  #other wise break out of the loop
#comparator(child, parent) use this method to to compare nodes.
