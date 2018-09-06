class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) - 1
    # or  index = self.get_size() - 1
    self._bubble_up(index)

  def delete(self):
    self.storage[0]= self.storage[len(self.storage) - 1]
    # self.storage[0]= self.storage[self.get_size() - 1]
    self._sift_down(0)


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while ((index - 1) // 2) > 0:
        if self.storage[(index - 1) // 2] < self.storage[index]:
            self.storage[(index - 1) // 2] = self.storage[index]
            self.storage[index] = self.storage[(index - 1) // 2]
        else:
            break
        index = (index - 1) // 2

  def _sift_down(self, index):
      while((index*2)+1) <= len(self.storage) - 1:
        if self.storage[(index*2)+1] > self.storage[index]:
            self.storage[(index*2)+1] = self.storage[index]
            self.storage[index] = self.storage[(index*2)+1]
        else:
            break
        index = (index*2) + 1
    
