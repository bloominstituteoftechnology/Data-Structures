class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    # # store what's at the front
    # front = self.storage[0]
    # # put the smallest value at the front, then remove it from our storage
    # self.storage[0] = self.storage[len(self.storage) - 1]
    # # call sift down
    # removed = self.storage.pop(len(self.storage)-1)
    # self._sift_down(0)
    # # return value
    # return removed
    if not self.storage:
      return False
    if self.get_size() == 1:
      return self.storage.pop()
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    temp = self.storage.pop()
    self._sift_down(0)
    return temp


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    ## while index greater than 0
    # get the parent (index - 1) // 2
    p = (index - 1) // 2
    ## if child is greater than parent--> comparator(child, parent)
    if index <= 0:
      return
    ## swap them
    elif self.storage[index] > self.storage[p]:
      self.storage[index], self.storage[p] = self.storage[p], self.storage[index]
      self._bubble_up(p)
    ## if not, then we're still inside the while loop, but we have nothing to do
    ## break

  def _sift_down(self, index):
    ## left child: 2 * index, + 1
    left = (2 * index) + 1
    # ## right child: 2 * index, + 2
    right = (2 * index) + 2
    da = index
    if self.get_size() > left and self.storage[da] < self.storage[left]:
      da = left
    if self.get_size() > right and self.storage[da] < self.storage[right]:
      da = right
    if da != index:
      self.storage[index], self.storage[da] = self.storage[da], self.storage[index]
      self._sift_down(da)


# test = Heap(1)

# test.insert(10)
# test.insert(9)
# test.insert(8)
# test.insert(7)

# test._sift_down(0)
# test.delete()