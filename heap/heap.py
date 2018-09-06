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
    return len(self.storage)

  def _bubble_up(self, index):
    parent = self.storage[floor((index - 1)/2)]
    child = self.storage[index]
    while parent:
      if child > parent:
        self.storage[floor((index - 1)/2)] = child
        self.storage[index] = parent

  def _sift_down(self, index):
    parent = self.storage[index]
    leftChild = self.storage[2*index + 1]
    rightChild = self.storage[2*index + 2]
    while leftChild:
      if parent < leftChild:
        self.storage[index] = leftChild
        self.storage[2*index + 1] = parent
      elif parent < rightChild:
        self.storage[index] = rightChild
        self.storage[2*index + 2] = parent
