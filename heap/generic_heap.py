class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = lambda y, x: x > y

  def insert(self, value):
    self.storage.append(value) #insert in the left most postion of the tree
    val_index = len(self.storage) - 1
    self._bubble_up(val_index)
  def delete(self):
    pass
  #store what is at the front
  #put the smallest value at the front, then remove it from our storage
  #call shift_down
  #return value

  def get_max(self):
    pass

  def get_size(self):
    pass
  #the size of array/tree

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1 ) // 2
      if self.storage[index] > self.storage[parent]:
          self.storage[index] , self.storage[parent] = self.storage[parent] , self.storage[index]
          index = parent #updating your new index
      else:
          break

  def _sift_down(self, index):
    pass
  #while index is less than max index
  #look at both children, choose the biggest
  #left child 2 * index + 1
  #right child 2 * index + 2
  #swap with that child,if the chosen one is larger update the index to the new location
  #other wise break out of the loop
#comparator(child, parent) use this method to to compare nodes.