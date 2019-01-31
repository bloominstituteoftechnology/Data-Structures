class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.size += 1
    self.storage.append(value)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass


new_heap = Heap()

print(new_heap.insert(10))