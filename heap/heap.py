class Heap:
  def __init__(self):
    self.storage = [0]
    self.current_size = 0 # length of array or size of heap

  def insert(self, value):
    self.storage.append(value)
    self.current_size += 1
    self._bubble_up(self.current_size)

  def delete(self):
    root_node = self.storage[1] 
    self.storage[1] = self.storage[self.current_size]
    # move last leaf node to top
    self.storage.pop() 
    self.current_size = self.current_size - 1
    # move the top node down
    self._sift_down(1)
    return root_node

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.current_size

  def _bubble_up(self, index):
    while index // 2 > 0:
      # if parent node is smaller than child node
      # for min heap, parent node is larger than child node
      # then swap
      if self.storage[index] > self.storage[index // 2]: 
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      # move one level up
      index = index // 2

  def _sift_down(self, index):
    def find_index(index):
      if index * 2 + 1 > self.current_size:
        return index * 2
      else:
        if self.storage[index * 2] < self.storage[index * 2 + 1]:
          return index * 2 + 1
        else:
          return index * 2 

    while (index * 2) <= self.current_size:
      child_index = find_index(index)
      if self.storage[index] < self.storage[child_index]:
        self.storage[index], self.storage[child_index] = self.storage[child_index], self.storage[index]
      index =  child_index
