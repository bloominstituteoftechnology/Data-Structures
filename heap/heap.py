class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # add value to storage
    self.storage.append(value)
    # Increase the size
    self.size += 1
    # bubble up helper will find correct spot in the heap
    self._bubble_up(self.size)

  def delete(self):
    # store max value in a variable
    val_ue = self.storage[1]
    # replace first element withthe last element in the heap
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove the last element from the heap
    self.storage.pop()
    # shift down moves element at index 1 down 
    self._shift_down(1)
    return val_ue

  def get_max(self):
    return self.storage[1]
  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # bubbling the node at the giving index until it gets to a valid place
    # also loop until there is no valid parent index
    while index // 2 > 0:
      # checking if elements parent value is less than current value 
      if self.storage[index // 2] < self.storage[index]:
        # Swap happens here
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      # Heap element found a good cosy place and stays here :D 
      else:
        break
      # updating index value to become parent index in order to continue up the heap
      index = index // 2

  def _shift_down(self, index):
    # shifting down until element reaches a cosy place
    while (index * 2) <= self.size:
      # determine which child is higher value
      x = self._max_child(index)
      # check if x is the current node needs swapping
      if self.storage[index] < self.storage[x]:
        # if TRUE then swap
        self.storage[index], self.storage[x] = self.storage[x], self.storage[index]
      else:
        break
      index = x

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      # getting child with the highest value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1