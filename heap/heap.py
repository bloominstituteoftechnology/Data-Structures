class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    self.storage.append(value)
    self.count += 1
    # need to write a bubble up function to put element in place
    pass

  def delete(self):

    pass

  def get_max(self):
    return self.storage[0]
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
