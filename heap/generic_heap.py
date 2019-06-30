class Heap:
  def __init__(self, comparator=None):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    removed = self.storage[0]
    del self.storage[0]
    self._sift_down(0)
    return removed

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[index] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      
      index = (index - 1) // 2


  #max heap
  def _sift_down(self, index):
    parent_index = index
    left_child = parent_index * 2 + 1
    right_child = parent_index * 2 + 2

    maxIndex = left_child if self.storage[left_child] > self.storage[right_child] else right_child

    while self.storage[parent_index ]< self.storage[maxIndex]:
      #swap parent and max child
      temp = self.storage[parent_index]
      self.storage[parent_index] = self.storage[maxIndex]
      self.storage[maxIndex] = temp

      #update index to max_childs index
      parent_index = maxIndex
      left_child = parent_index * 2 + 1
      right_child = parent_index * 2 + 2

      #check to see if left and right exist
      if self.storage[maxIndex] > self.storage[index]:
        maxIndex = left_child if self.storage[left_child] > self.storage[right_child] else right_child
