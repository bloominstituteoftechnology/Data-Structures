class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    index=self.get_size()
    self.storage.append(value)
    self._bubble_up(index)

  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index-1)//2>=0:
      if self.storage[index]>self.storage[(index-1)//2]:
        placeholder=self.storage[(index-1)//2]
        self.storage[(index-1)//2]=self.storage[index]
        self.storage[index]=placeholder
        index=((index)-1)//2
      else:
        break

  def _sift_down(self, index):
    pass
