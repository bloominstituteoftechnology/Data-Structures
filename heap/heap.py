class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Append the value to the end of the list
    self.storage.append(value)

    # Get the size of the list
    size = self.get_size()

    # Call bubble up to move the corresponding nodes/values to
    # have the max value on top
    self._bubble_up(size - 1)

  def delete(self):
    # set indexa to the first item in the list
    indexa = self.storage[0]

    # Get the size of the list
    size = self.get_size()

    # Set the first item in the list to the next to last
    self.storage[0] = self.storage[size - 1]

    # Then pop the last element off
    self.storage.pop()

    # Then sift down
    self._sift_down(0)

    return indexa

  def get_max(self):
    # Return the first element in the list, should always be max
    return self.storage[0]

  def get_size(self):
    # Return the size of the list
    return len(self.storage)

  def _bubble_up(self, index):
    # Continue while the value is greater or equal to 0
    while (index - 1) // 2 >= 0:

      # If value is less than, set the index of the storage to
      # the new index
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = \
        self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    # 2n + 1, 2n + 2 formula for child
    size = len(self.storage)
    while index * 2 + 1 <= size - 1:
      
      # Find the larger of the two children
      max_child = None
      if index * 2 + 2 > size - 1:
        max_child = index * 2 + 1
      else:
        # Set max child to the index to the child node
        # that has the larger value
        max_child = index * 2 + 1 if self.storage[index * 2 + 1] > \
        self.storage[index * 2 + 2 ] else index * 2 + 2

      # Check to see if we need to swap
      if self.storage[index] < self.storage[max_child]:
        self.storage[index], self.storage[max_child] = \
        self.storage[max_child], self.storage[index]
      
      # Set index to the max child
      index = max_child
