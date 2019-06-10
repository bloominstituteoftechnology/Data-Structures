class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    i = 0
    put = False
    while True:
      for j in range(2**i - 1, 2**(i + 1)):
        if j < self.get_size():
          if self.storage[j] < value:
            self.storage.insert(j, value)
            put = True
            break
      if put:
        break
    if not put:
      self.storage.append(value)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
