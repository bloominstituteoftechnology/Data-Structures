class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    if len(self.storage) == 0:
      self.storage.append(value)
      return
    
    self.storage.append(value)

    childIndex = len(self.storage) - 1
    parentIndex = self._bubble_up(childIndex)

    while self.storage[childIndex] > self.storage[parentIndex]:
      
      tempChild = self.storage[childIndex]
      self.storage[childIndex] = self.storage[parentIndex]

      self.storage[parentIndex] = tempChild

      childIndex = parentIndex
      parentIndex = self._bubble_up(childIndex)
      if childIndex or parentIndex < 0:
        return


  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # Finds parent index of the child
    parentIndex = (index - 1) // 2
    return parentIndex

  def _sift_down(self, index):
    # Finds the child index of the parent
    childIndex = 0
    if index % 2 == 0:
      childIndex = 2 * index + 2
    else:
      childIndex = 2 * index + 1
    return childIndex
