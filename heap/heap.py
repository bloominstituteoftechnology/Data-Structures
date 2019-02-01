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


  def _sift_down(self, index):
