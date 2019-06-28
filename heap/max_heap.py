class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    
    if self.storage[0]:
      val = self.storage[0]

      if self.get_size() <= 1:
        self.storage = []
      else:
        # Set index 0 to the last value in list, and remove last
        self.storage[0] = self.storage.pop(self.get_size()-1)
        self._sift_down(0)
      return val

  def get_max(self):
    if self.get_size() >= 1:
      return self.storage[0]
    else:
      return None

  def get_size(self):
    return len(self.storage)

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
    # Check if index is greater than 0
    # Calc left & right
    # Determine > of left/right
    # If > left/right > index value - swap

    while index < self.get_size():
      left = (2 * index) + 1 if (2 * index) + 1 < self.get_size() else index
      right = (2 * index) + 2 if (2 * index) + 2 < self.get_size() else index
      maxIndex = left if self.storage[left] > self.storage[right] else right

      if self.storage[index] < self.storage[maxIndex]:
        # Swap them!
        self.storage[index], self.storage[maxIndex] = self.storage[maxIndex], self.storage[index]
        index = maxIndex
      else:
        break
