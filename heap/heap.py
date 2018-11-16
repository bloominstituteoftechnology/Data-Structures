class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)  # call _bubble_up passing in index of the value that was just inserted

  # def delete(self):
  #   self.storage[0] = self.storage[-1]


  # def left_index(self, index):
  #   return index * 2 + 1

  # def left_val(self, index):
  #   return self.storage[self.left_index(index)]

  # def right_index(self, index):
  #   return index * 2 + 2
  
  # def right_val(self, index):
  #   return self.storage[self.right_index(index)]

  def parent_index(self, index):
    return (index - 1) // 2 

  def parent_val(self, index):
    return self.storage[self.parent_index(index)]

  def get_max(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    
    while index > 0 and self.storage[index] > self.parent_val(index):  # If not at root & if current value greater than parent value
      pindex = self.parent_index(index)                               

      self.storage[index], self.storage[pindex] = \
        self.storage[pindex], self.storage[index]                      # Swap current value and parent value like a,b = b,a
      index = pindex
      print(self)

  # def get_max_child_index(self, index):
  #   # if right is out of bounds, left must be bigger
  #   if self.right_index(index) >= len(self.storage):
  #     return self.left_index(index)

  #   if self.right_val(index) > self.left_val(index):
  #     return self.right_index(index)

  #   return self.left_index(index)

  # def _sift_down(self, index):
  #   while self.left_index(index) < len(self.storage):
  #     max_child_index = self.get_max_child_index(index)

  #     if self.storage[index] < self.storage[max_child_index]:
  #       self.storage[index], self.storage[max_child_index] = \
  #         self.storage[max_child_index], self.storage[index]
  #       index = max_child_index

  #     else:
  #       break

  # def __str__(self):
  #     rv = "Heap:\n"

  #     l = 1
  #     c = 0

  #     for i in range(len(self.storage)):
  #       rv += str(self.storage[i]) + "  "

  #       c += 1

  #       if c >= l:
  #         rv += "\n" + "  " * l
  #         c = 0
  #         l *= 2

  #     rv += "\n"

  #     return rv
