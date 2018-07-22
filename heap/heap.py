class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    valueIndex = len(self.storage)
    self._bubble_up(valueIndex)

  def delete(self):
    if len(self.storage) == 1:
      return None
    removed_placeholder = self.storage[1]

    # overwrite top/max value with value at the end of array
    self.storage[1] = self.storage[self.size]
    self.storage.pop() #remove the last element which was copied to front
    self.size -= 1 # reduce size by 1

    if self.size > 0:
      self._sift_down(1) #sift the previouly last value to a lower place

    return removed_placeholder

  def get_max(self):
    if self.size > 0:
      return self.storage[1]
    else:
      return None

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # while storage[index] has a parent "node"
    while index // 2 > 0:
      # if parent is < child
      if self.storage[index//2] < self.storage[index]:
        # pythonic way of switching elements in array
        self.storage[index//2], self.storage[index] = self.storage[index], self.storage[index//2]
      # if parent is not < child, then break while-loop
      else:
        break
      # reset condition for while loop
      index = index // 2


  def _sift_down(self, index):
    pass
