class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    indexOfValue = len(self.storage) -1
    while(True):
      indexOfValue = self._bubble_up(indexOfValue)
      if indexOfValue is False:
        break

  def delete(self):
    if self.get_size() == 1:
      return self.storage.pop()
    oldTop = self.storage[0]
    self.storage[0]= self.storage.pop()
    indexOfValue = 0
    while(True):
      indexOfValue = self._sift_down(indexOfValue)
      if indexOfValue is False:
        return oldTop

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return False
    child = self.storage[index]
    parent = self.storage[(index - 1)//2]
    if child > parent:
      self.storage[index] = parent
      self.storage[(index - 1)//2] = child 
      return (index - 1)//2
    return False

  def _sift_down(self, index):
    try:
      leftChild = self.storage[(2*index) +1] 
    except IndexError:
      leftChild = 0
    try:
      rightChild = self.storage[(2*index) +2]
    except IndexError:
      rightChild = 0
    if leftChild > rightChild:
      if leftChild > self.storage[index]:
        self._bubble_up((2*index) +1)
        return (2*index) +1

    if rightChild > self.storage[index]:
      self._bubble_up((2*index) +2)
      return (2*index) +2
    return False
