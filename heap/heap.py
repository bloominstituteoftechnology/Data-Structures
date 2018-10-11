class Heap:
  def __init__(self):
    self.storage = []

    #   [1,
    #   2,3
    # 4,5,6,7]

  def insert(self, value):
    return self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    val = self.storage[0]
    # replace first storage element with the last element in heap
    self.storage[0] = self.storage[len(self.storage) -1]
    # remove last element in heap
    self.storage.pop()
    self._sift_down(0)
    return val

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # index of element that will be moving up the heap
    # keep bubbling the element at the given index up the heap until valid spot is reached
    while (index - 1) // 2 >= 0:
      # check to see if el's parent value is less than cuurent value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        #  swap values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # update index to be parent index so that we continue up the heap
      index = (index - 1) // 2


  def _sift_down(self, index):
    # while index * 2 + 1 <= len(self.storage) - 1:
    #   # figure out larger of the two children
    #   mc = self._max_child(index)
    #   #  check to see if swap needed
    #   if self.storage[index] < self.storage[mc]:
    #     self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
    pass