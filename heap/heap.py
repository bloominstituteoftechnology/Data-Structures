class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.size += 1
    self.storage.append(value)

  def delete(self):
    self.size -= 1

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass


new_heap = Heap()
new_heap.insert(5)
new_heap.insert(10)
new_heap.insert(2)
print(new_heap.get_size())