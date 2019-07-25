class Heap:
  def __init__(self):
    self.storage = []

  def __str__(self):
    return str(self.storage)

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    if self.get_size() < 1:     # empty list, bail
      return None
    if self.get_size() == 1:    # one-item list
      return self.storage.pop(0)
    ret = self.storage[0]
    self.storage[0] = self.storage.pop(self.get_size() - 1)
    if self.get_size() > 1:     # only sift down if we have more than one item left
      self._sift_down(0)
    return ret

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    while (self.storage[index] > self.storage[(index-1) // 2] and index > 0):
      self.storage[index], self.storage[(index-1) // 2] = self.storage[(index-1) // 2], self.storage[index]
      index = (index-1) // 2

  def _get_bigger(self, x, y):
    if x > y:
      return 1
    else:
      return 2

  def _sift_down(self, index):
    limit = self.get_size() - 1
    if index*2 + 2 > limit:
      if index*2 + 1 == limit:
        if self.storage[index] < self.storage[index * 2 + 1]:
          self.storage[index * 2], self.storage[index * 2 + 1] = self.storage[index * 2 + 1], self.storage[index * 2]
      return
    x = self._get_bigger(self.storage[index*2 + 1], self.storage[index*2 + 2])
    if self.storage[index] < self.storage[index*2 + x]:
      self.storage[index], self.storage[index*2 + x] = self.storage[index*2 + x], self.storage[index]
      self._sift_down(index*2 + x)

heap = Heap()

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
