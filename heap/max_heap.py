import math

class Heap:
  def __init__(self):
    self.storage = []

  def _bubble_up(self, index):
# keep bubbling up until we've either reached the top of the heap
# or we've reached a point where the parent is higher prio
    while index > 0:
    # on a single bubble up iteration
    # get the parent index
        parent = (index - 1) // 2
    # compare the child against the value of the parent
    # if the child's value is higher prio than its parent's value
        if self.storage[index] > self.storage[parent]:
        # swap them
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # update the child's index to be the new index it is now at
            index = parent
        # otherwise, child is at a valid spot
        else:
    # stop bubbling up
            break

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def _sift_down(self, index):
    my_index = index
    if len(self.storage) < 2:
        return
    # determine the indices of index's children
    # determine which child has a larger value
    # if the child has a larger value than the parent, the parent and child elements are swapped
    # update the index value
    # base case: index of index's left child is out of range or neither child is larger than the parent
    while (2 * index) + 1 < len(self.storage):
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        if right_child > len(self.storage) - 1:
            if self.storage[left_child] > self.storage[index]:
                swapped_value = self.storage[left_child]
                self.storage[left_child] = self.storage[index]
                self.storage[index] = swapped_value
                index = left_child
        elif self.storage[left_child] > self.storage[right_child]:
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
