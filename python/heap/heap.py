class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    tmp = self.storage[1]
    self.storage[1] = self.storage[-1]
    self.storage.pop()
    self.size -= 1
    self._sift_down(1)
    return tmp

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, i):
    if i == 1:
      return
    if self.storage[i // 2] < self.storage[i]:
      self.swap(i, i // 2)
      self._bubble_up(i // 2)

  def _sift_down(self, i):
    l = 2 * i
    r = 2 * i + 1
    if r <= self.size:
        if self.storage[l] > self.storage[r]:
          if self.storage[i] < self.storage[l]:
            self.swap(i, l)
            self._sift_down(l)
        else:
          if self.storage[i] < self.storage[r]:
            self.swap(i, r)
            self._sift_down(r)
    elif self.size == 2:
      if self.storage[i] < self.storage[l]:
        self.swap(i, l)

  def swap(self, x, y):
    a = self.storage[x]
    b = self.storage[y]
    self.storage[y] = a
    self.storage[x] = b