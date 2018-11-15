class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    self.storage.pop(0)
    self.storage.insert(0,self.storage[len(self.storage)-1])
    self.storage.pop()
    index = 0
    while self.storage[index]<self.storage[(2*index)+1] or self.storage[index]<self.storage[(2*index)+2]:
      if self.storage[index] < self.storage[(2*index)+1]:
        temporary = self.storage[index]
        self.storage[index] = self.storage[(2*index)+1]
        self.storage[(2*index)+1] = temporary
        index = (2*index)+1
      else:
        temporary = self.storage[index]
        self.storage[index] = self.storage[(2*index)+2]
        self.storage[(2*index)+2] = temporary
        index = (2*index)+2

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if self.storage[index] > self.storage[int((self.get_size()-2)/2)]:
      temporary = self.storage[int((self.get_size()-2)/2)]
      self.storage[int((self.get_size()-2)/2)] = self.storage[index]
      self.storage[self.get_size()-1] = temporary

  def _sift_down(self, index):
    if (2*index)+1 < self.get_size():
      if self.storage[index] < self.storage[(2*index)+1]:
        temporary = self.storage[index]
        self.storage[index] = self.storage[(2*index)+1]
        self.storage[(2*index)+1] = temporary
        return (2*index)+1
    elif (2*index)+2 < self.get_size:
      if self.storage[index] < self.storage[(2*index)+2]:
        temporary = self.storage[index]
        self.storage[index] = self.storage[(2*index)+2]
        self.storage[(2*index)+2] = temporary
        return (2*index)+2
    else:
      print('Error in _sift_down()')
      return -1
