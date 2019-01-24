class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # append at first convenient place, aka end of storage
    self.storage.append(value)
    # shuffle value to appropriate place
    self._bubble_up(len(self.storage) - 1)
    

  def delete(self):
    # only deletes first item in self.storage
    temp = self.storage[0]
    self.storage.pop()
    

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = (index - 1) // 2
    
    if parent_index >= 0 and self.storage[parent_index] < self.storage[index]:
      temp = self.storage[parent_index]
      self.storage[parent_index] = self.storage[index]
      self.storage[index] = temp
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    pass
