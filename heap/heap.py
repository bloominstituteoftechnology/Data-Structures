class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # append value to storage
    self.storage.append(value)
    #increment size
    self.size += 1
    # bubble up
    self._bubble_up(self.size)
    #pass

  def delete(self):
    # if empty return none
    if self.size == 0:
      return None
    # create variables for the storage top and storage end
    storage_top = self.storage[1]
    storage_end = self.storage.pop()
    # decrement the size
    self.size -= 1
    # if size zero return storage top
    if self.size == 0:
      return storage_top

    # set storage of index 1 to storage end
    self.storage[1] = storage_end
    # shift down
    self._sift_down(1)
    #return storage top
    return storage_top
    #pass

  def get_max(self):
    # return the storage at index 1
    return self.storage[1]
    #pass

  def get_size(self):
    # return size
    return self.size
    #pass

  def _bubble_up(self, index):
    # set index of parent to index divided by 2 ( as whole number ) see : https://www.geeksforgeeks.org/division-operator-in-python/
    # if the parent index is equal to zero return to the caller
    index_of_parent = index//2
    if index_of_parent == 0:
      return
    # if the storage at the index of parent is less than the storage of index swap the parent with the current node
    # and do a recursive call to bubble up at index of parent
    if self.storage[index_of_parent] < self.storage[index]:
      temp = self.storage[index_of_parent]
      self.storage[index_of_parent] = self.storage[index]
      self.storage[index] = temp
      self._bubble_up(index_of_parent)
    #pass

  def _sift_down(self, index):
    # set index left to index if 2 times the index is greater than size otherwise set it to two times index
    index_left = index if 2 * index > self.size else 2 * index
    # set index right to index if 2 times the index plus 1 is greater than size otherwise set it to two times index plus one
    index_right = index if 2 * index + 1 > self.size else 2 * index + 1
    # set index of child to index left if the storage at index left is greater than the storage at index right otherwise return index right
    index_of_child = index_left if self.storage[index_left] > self.storage[index_right] else index_right
    # if the index of child is equal to the index then return to caller
    if index_of_child == index:
      return
    # if the storage at index of child is greater than the storage at index 
    if self.storage[index_of_child] > self.storage[index]:
    # swap the storage value at index with the storage value at index of child and do a recursive call to sift down
      temp = self.storage[index]
      self.storage[index] = self.storage[index_of_child]
      self.storage[index_of_child] = temp
      self._sift_down(index_of_child)
    #pass