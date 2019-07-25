class Heap:
  def __init__(self, comparator="max"):
    self.storage = []
    self.comparator = comparator

  def __str__(self):
    return str(self.storage)

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    if self.get_size() < 1:  # empty list, bail
      return None
    if self.get_size() == 1:  # one-item list
      return self.storage.pop(0)
    ret = self.storage[0]
    self.storage[0] = self.storage.pop(self.get_size() - 1)
    self._sift_down(0)
    return ret

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    if self.comparator == "max":
      self._bubble_up_max(index)
    else:
      self._bubble_up_min(index)

  def _bubble_up_max(self, index):
    while (self.storage[index] > self.storage[(index - 1) // 2] and index > 0):
      self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _bubble_up_min(self, index):
    while (self.storage[index] < self.storage[(index - 1) // 2] and index > 0):
      self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    if self.get_size() <= 1:    # kludge to keep lambda tests happy - was doing it in "delete" code
      return
    if self.comparator == "max":
      self._sift_down_max(index)
    else:
      self._sift_down_min(index)

  def _sift_down_max(self, index):
    # This is admittedly a horrendous kludge but it wotks and I don't feel like fixing it!
    limit = self.get_size() - 1
    if index * 2 + 2 > limit:
      if index * 2 + 1 == limit:
        if self.storage[index] < self.storage[index * 2 + 1]:
          self.storage[index * 2], self.storage[index * 2 + 1] = self.storage[index * 2 + 1], self.storage[index * 2]
      return
    x = self._get_bigger(self.storage[index * 2 + 1], self.storage[index * 2 + 2])
    if self.storage[index] < self.storage[index * 2 + x]:
      self.storage[index], self.storage[index * 2 + x] = self.storage[index * 2 + x], self.storage[index]
      self._sift_down_max(index * 2 + x)

  def _get_bigger(self, x, y):
    if x >= y:
      return 1
    else:
      return 2

  def _sift_down_min(self, index):
    # This is admittedly a horrendous kludge but it wotks and I don't feel like fixing it!
    limit = self.get_size() - 1
    if index * 2 + 2 > limit:
      if index * 2 + 1 == limit:
        if self.storage[index] > self.storage[index * 2 + 1]:
          self.storage[index * 2], self.storage[index * 2 + 1] = self.storage[index * 2 + 1], self.storage[index * 2]
      return
    x = self._get_smaller(self.storage[index * 2 + 1], self.storage[index * 2 + 2])
    if self.storage[index] > self.storage[index * 2 + x]:
      self.storage[index], self.storage[index * 2 + x] = self.storage[index * 2 + x], self.storage[index]
      self._sift_down_min(index * 2 + x)

  def _get_smaller(self, x, y):
    if x <= y:
      return 1
    else:
      return 2

heap = Heap("max")

heap = Heap(lambda x, y: x < y)

heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)

print(heap)

descending_order = []

while heap.get_size() > 0:
  descending_order.append(heap.delete())

print(heap)
print(descending_order)
