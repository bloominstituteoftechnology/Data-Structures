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
    retval = self.storage[1]

    self.storage[1] = self.storage[self.size]
    self.size -= 1

    self.storage.pop()

    self._sift_down(1)

    return retval

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):

    while index //2 >0:

      if self.storage[index // 2] <self.storage[index]:
        self.storage[index //2 ], self.storage[index] = self.storage[index], self.storage[index // 2]

    

  def _sift_down(self, index):
    pass
