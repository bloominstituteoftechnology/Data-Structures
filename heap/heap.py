class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    return self._bubble_up(self.get_size() - 1)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    storage = self.storage
    while index // 2 > 0:
      if self.heapList[index] < self.heapList[index // 2]:
         tmp = self.heapList[index // 2]
         self.heapList[index // 2] = self.heapList[index]
         self.heapList[index] = tmp
      index = index // 2

  def _sift_down(self, index):
    pass
