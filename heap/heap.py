class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1 
    self._bubble_up(self.size)

  def delete(self):
    if self.size == 0:
      return None
    elif self.size == 1:
      self.size -= 1
      return self.storage.pop()
    else: 
      new = self.storage.pop()
      old = self.storage[1]
      self.storage[1] = new
      self.size -= 1
      self._sift_down(1)
      return old

  def get_max(self):
    index = 1 * 2 +1 
    if self.size <= 3:
      return self.storage[1]
    if self.storage[index] > self.storage[1]:
      while True:
        if index > self.size:
          return self.storage[math.floor(index / 2)]
        else:
          if self.storage[index * 2 + 1] > self.storage[index]:
            index = index * 2 + 1
          else: return self.storage[index]

  def get_size(self): 
    return

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
