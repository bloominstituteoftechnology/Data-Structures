class Heap:
  def __init__(self):
    
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    print('*************************')
    print('Heap after inserting %(value)s: ' % {"value": value})
    print(self)
    self._bubble_up(len(self.storage) - 1)  # call _bubble_up passing in index of the value that was just inserted

  # delete method needs to remove the top node, which needs to be replaced
  # replace top node (index 0) with the value at the last index (it's also the smallest value)
  # that way only that one value needs to percolate down back to its original position
  def delete(self):
    print('*************************')
    print('delete called')
    print('Heap before delete: ')
    print(self)
    print('Heap after delete: ')
    print(self)

    deleted_item = self.storage[0]
    self.storage[0] = self.storage[-1]  # Replace value at index 0 with the value from index -1 aka end of the list
    self.storage.pop()                  # Shorten list by 1 by popping off last index
    self._sift_down(0)
    return deleted_item

  def left_index(self, index):
    return index * 2 + 1

  def left_val(self, index):
    return self.storage[self.left_index(index)]

  def right_index(self, index):
    return index * 2 + 2
  
  def right_val(self, index):
    return self.storage[self.right_index(index)]

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
      print('Heap after bubbling: ')
      print(self)

  def get_max_child_index(self, index):
    # if this stament is true, right is out of bounds
    if self.right_index(index) >= len(self.storage): # if right is out of bounds, left must be bigger
      return self.left_index(index)

    if self.right_val(index) > self.left_val(index):
      return self.right_index(index)

    return self.left_index(index)

  def _sift_down(self, index):
    while self.left_index(index) < len(self.storage): # if there is a left child
      max_child_index = self.get_max_child_index(index)

      if self.storage[index] < self.storage[max_child_index]:
        self.storage[index], self.storage[max_child_index] = \
          self.storage[max_child_index], self.storage[index]  # Swap like a,b = b,a
        index = max_child_index

      else:
        break

  def __str__(self):
      rv = "Heap:\n"

      l = 1
      c = 0

      for i in range(len(self.storage)):
        rv += str(self.storage[i]) + "  "

        c += 1

        if c >= l:
          rv += "\n" + "  " * l
          c = 0
          l *= 2

      rv += "\n"

      return rv
