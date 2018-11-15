# I found this site to be a great resource: https://algorithms.tutorialhorizon.com/binary-min-max-heap/
# and this helped port it over to Python: https://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html

class Heap:
  def __init__(self):
    # initialize the array at index 1 by having in index[0] value of 0
    # "this zero is not used, but is there so that simple integer division can be used in later methods."
    self.storage = [0]
    # initialize the heap size to 0
    self.size = 0

  def insert(self, value):
    # add the value to storage
    self.storage.append(value)
    # increase the size of the heap
    self.size += 1
    # bubble up for proper ordering, starting at last index i.e. self.size
    # this last index value is the newly added value via .append()
    self._bubble_up(self.size)
    # pass

  def delete(self):
    # edge case for an empty heap
    if self.size == 0:
      return None
    pass

  def get_max(self):
    return self.storage[1]
    pass

  def get_size(self):
    return self.size
    # pass

  def _bubble_up(self, index):
    while (index // 2) > 0:
      print('bubbling', index // 2)
      if self.storage[index] < self.storage[index // 2]:
        # store the parent index in temp
        temp = self.storage[index // 2]
        # swap the index values
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = temp
      # this final operation causes the index to 'bubble' through the while loop into each parent node
      index = index // 2
    # pass

  # finds the lowest value's index in the heap to use in sift_down
  def min_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      if self.storage[index*2] < self.storage[index*2+1]:
        return index * 2
      else:
        return index * 2 + 1

  def _sift_down(self, index):
    # traverse down the heap with while loop
    while (index * 2) <= self.size:
      print('sifting')
      # collect the index of the lowest value via min_child()
      lowest = self.min_child(index)
      # compare the values of the current index with the values in the last index
      if self.storage[index] > self.storage[lowest]:
        # perform a swap
        temp = self.storage[index]
        self.storage[index] = self.storage[lowest]
        self.storage[lowest] = temp
      
      index = lowest