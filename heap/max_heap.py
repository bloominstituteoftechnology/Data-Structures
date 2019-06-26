class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # 1. Check if index is greater than zero
    # 2. Get parent index
    # 3. If current value > parent: Swap
    # 4. Otherwise leave it & break

    while index > 0:
      parent = (index - 1) // 2

      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent # Don't forget to update new index!
      else:
        break

  def _sift_down(self, index):
    pass
