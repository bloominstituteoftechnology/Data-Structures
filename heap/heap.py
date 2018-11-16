class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    self.storage.pop(0)
    storage_length = len(self.storage)-1
    if storage_length < 0:
      return
    last_element = self.storage[storage_length]
    self.storage.insert(0,last_element)
    self.storage.pop()
    index = 0
    keep_sifting = True
    storage_length = len(self.storage)
    while keep_sifting:
      index = self._sift_down(index)
      if index == -1:
        break
      keep_sifting = index < storage_length

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
    left_child_index = (2*index)+1
    storage_length = len(self.storage)
    parent = self.storage[index]
    right_child_index = (2*index)+2
    right_child = 0
    if right_child_index < storage_length-1:
      right_child = self.storage[right_child_index]
    else:
      right_child = 0
    if left_child_index < storage_length:
      left_child = self.storage[left_child_index]
      if parent < left_child and left_child>right_child:
        temporary = parent
        self.storage[index] = left_child
        self.storage[left_child_index] = temporary
        return left_child_index
      elif right_child_index < storage_length:
        if parent < right_child:
          temporary = parent
          self.storage[index] = right_child
          self.storage[right_child_index] = temporary
          return right_child_index
        else:
          return -1
      else:
        return -1
    else:
      return -1