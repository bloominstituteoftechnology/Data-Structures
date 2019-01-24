class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    return self._bubble_up(self.get_size() - 1)

  def delete(self):
    returnvalue = self.storage[1]
    self.storage[1] = self.storage[self.get_size()]
    self.get_size = self.get_size() - 1
    self.storage.pop()
    self._sift_down(1)
    return returnvalue

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index] < self.storage[index // 2]:
         tmp = self.storage[index // 2]
         self.storage[index // 2] = self.storage[index]
         self.storage[index] = tmp
      index = index // 2

  def _sift_down(self, index):
    max_child = None
    if index * 2 + 1 >= self.get_size():
        return
    elif index * 2 + 2 >= self.get_size():
        max_child = index * 2 + 1
    elif storage[index * 2 + 1] > storage[index * 2 + 2]:
        max_child = index * 2 + 1
    else:
        max_child = index * 2 + 2

    if storage[index] < storage[max_child]:
        storage[index], storage[max_child] = storage[max_child], storage[index]
        self._sift_down(max_child)
    else:
        return
