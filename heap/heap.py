class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if len(self.storage) > 0:
      deleted = self.storage.pop(0)
      if len(self.storage) > 0:
        root_replace = self.storage.pop()
        self.storage.insert(0, root_replace)
        self._sift_down(0)
      return deleted

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # index is the index of the element that will be moving up the heap
    # keep bubbling the element at the given index up the heap until reaches a valid spot
    while (index - 1) // 2 >= 0:
      # check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap the values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # update the index to be the parent's index so that we can continue moving up
      index = (index - 1) // 2

  def _sift_down(self, index):
    # index is the index of the element that will be moving down the heap
    # keep sifting the element at the given index down the heap until it reaches a valid spot
    # while self.storage[(2 * index + 1)]:
    # if (2 * index + 2) < len(self.storage):
    #   # check to see which child is larger
    #   if self.storage[(2 * index + 1)] > self.storage[(2 * index + 2)]:
    #     # check to see if the child is larger than the parent
    #     if self.storage[(2 * index + 1)] > self.storage[index]:
    #       #swap values
    #       self.storage[index], self.storage[(2 * index + 1)] = self.storage[(2 * index + 1)], self.storage[index]
    #     index = 2 * index + 1
    #   elif self.storage[(2 * index + 1)] <= self.storage[(2 * index + 2)]:
    #     if self.storage[(2 * index + 2)] > self.storage[index]:
    #       # swap values
    #       self.storage[index], self.storage[(2 * index + 2)] = self.storage[(2 * index + 2)], self.storage[index]
    #     index = 2 * index + 2


    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] <  self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    # check if the right child index is out of bouns of our strage array
    if index * 2 + 2 > len(self.storage) - 1:
      # return the left child index
      return index * 2 + 1
    else:
      # return the index of child node that has larger value
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2 