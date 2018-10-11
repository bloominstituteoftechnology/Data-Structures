class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.insert(len(self.storage), value)
    self._bubble_up()

  def delete(self):
    self.storage.pop(0)
    self._sift_down()

  def get_max(self):
    pass

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
