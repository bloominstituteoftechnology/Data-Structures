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
    if index == 0:
    # if self.storage[index] == 0:
      current_node = self.storage.index(self.storage[-1])
    else: 
      current_node = index

    if len(self.storage) == 1:
      return

    parent_index = (current_node // 2)

    parent_value = self.storage[parent_index]

    if self.storage[current_node] > parent_value:
      temp = self.storage[parent_index] 
      self.storage[parent_index] = self.storage[current_node]
      self.storage[current_node] = temp
      current_node = parent_index
      return self._bubble_up(current_node)


  def _sift_down(self, index):
    pass
