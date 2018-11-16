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
    self.size = self.size + 1
    # bubble up for proper ordering, starting at last index i.e. self.size
    # this last index value is the newly added value via .append()
    self._bubble_up(self.size)
    # pass

  def delete(self):
    root = self.storage[1]
    bottom = self.storage.pop()
    self.size = self.size - 1
    if self.size == 0:
      return root
    self.storage[1] = bottom
    self._sift_down(1)
    return root
    # pass

  def get_max(self):
    return self.storage[1]
    # pass

  def get_size(self):
    return self.size
    # pass

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index] > self.storage[index // 2]:
        # store the parent index in temp
        temp = self.storage[index // 2]
        # swap the index values
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = temp
      # this final operation causes the index to 'bubble' through the while loop into each parent node
      index = index // 2
    # pass

  def _sift_down(self, index):
    # collect the left and right children's indices of the given index
    left_child = index * 2
    right_child = (index * 2) + 1
    # ensure we're not exceeding the size of the heap
    if left_child > self.size:
      return
    if right_child <= self.size:
      if self.storage[index] < self.storage[left_child] or self.storage[index] < self.storage[right_child]:
        # find the largest child between left and right
        largest_child = right_child if (self.storage[right_child] > self.storage[left_child]) else left_child
        # swap the largest value with the current index
        self.storage[index], self.storage[largest_child] = self.storage[largest_child], self.storage[index]
        # recursively sift the low values down
        return self._sift_down(largest_child)
      else:
        return
    else:
      if self.storage[index] < self.storage[left_child]:
        # swap
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
        return self._sift_down(left_child)
      else:
        return