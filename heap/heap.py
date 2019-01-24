class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    length = len(self.storage) + 1
    self._bubble_up(length)

  def delete(self):
    max_value = self.storage[0]
    length = len(self.storage) - 1
    self.storage[0] = self.storage[length]
    self.storage.pop()
    self._sift_down(0)
    return max_value

  def get_max(self):
    # max_value = self.storage[0]
    # for item in self.storage:
    #   if item > max_value:
    #     max_value = item
    # return max_value
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index] < self.storage[index // 2]:
        temp = self.storage[index // 2]
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = temp
      index = index // 2

  def _sift_down(self, index):
    pass


# left = 2index + 1 

# right = 2index + 2

# parent = floor(  (index - 1) / 2   )

"""
Store a reference to the first heap element
Set the value of the first heap element to the value of the last heap element
Pop from the heaps storage array to remove the last heap elememt
In a loop
  Have the new first heap eleemt check its two children using the given formulas
  If either of the elemnts children are larger, swap the heap value of the parent node
   with the value of the larger childs value via their respective indicies
Continue this loop until the element is in a spot where neither of its children are larger than it
Or its reached a spot where it has no children
"""