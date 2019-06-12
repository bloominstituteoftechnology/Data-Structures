import math

class Heap:
  def __init__(self):
    self.storage = []

  def _bubble_up(self, index):
    while True:
        parent = math.floor((index - 1) / 2)
        if parent >= 0:
            if self.storage[index] > self.storage[parent]:
                swapped_value = self.storage[parent]
                self.storage[parent] = self.storage[index]
                self.storage[index] = swapped_value
                index = parent
                print("Meets condition \n\n\n\n")
                print(index)
            else:
                break
        else:
            break

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(-1)

  def _sift_down(self, index):
    my_index = index
    # determine the indices of index's children
    # determine which child has a larger value
    # if the child has a larger value than the parent, the parent and child elements are swapped
    # update the index value
    # base case: index of index's left child is out of range or neither child is larger than the parent
    while index < len(self.storage):
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        if self.storage[left_child] > self.storage[right_child]:
            if self.storage[left_child] > self.storage[index]:
                swapped_value = self.storage[left_child]
                self.storage[left_child] = self.storage[index]
                self.storage[index] = swapped_value
                index = left_child
            else:
                break
        elif self.storage[right_child] > self.storage[index]:
            swapped_value = self.storage[right_child]
            self.storage[right_child] = self.storage[index]
            self.storage[index] = swapped_value
            index = right_child
        else:
            break


  def delete(self):
    swapped_value = self.storage[0]
    self.storage[0] = self.storage[-1]
    self.storage[-1] = swapped_value
    self.storage.pop(-1)
    self._sift_down(0)
    return swapped_value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)
