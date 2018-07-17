import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # insert the value at the end of the storage array
    self.storage.append(value)
    self.size += 1

    # pass the index in the bubble up
    self._bubble_up(self.get_size()- 1)


  # removes the maximum value from the heap
  def delete(self):
    # check if heap is not empty
    if not self.size: return None 
    
    # get a max
    max = self.storage.pop()
    
    # check if the heap has only one element
    if self.size == 1:
      self.size -= 1
    else:
      # move the last element in the heap to the root temporarily
      last_item = self.storage.pop()
      self.storage.insert(1, last_item)

      # call sift_down on the root element to re-arrange the heap
      self._sift_down(1)

    # return max
    return max


  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # parents index
    parent_index = math.floor(index / 2)

    # check if the value at this index needs to be shifted up
    if self.storage[parent_index] < self.storage[index]:
      # swap the values at the index and parentIndex
      self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]

      # recursively call bubble up
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_child_index = index * 2
    rightt_child_index = index * 2 + 1

    # figure out the larger child
    max_child_index = None 
    
    if self.storage[left_child_index]:
      if not self.storage[rightt_child_index]:
        max_child_index = left_child_index
      elif self.storage[rightt_child_index]:
        max_child_index = left_child_index if self.storage[left_child_index] else rightt_child_index

      # check if we need to swap our current value with its larger child
      if self.storage[index] < self.storage[max_child_index]:
        self.storage[max_child_index], self.storage[index] = self.storage[index], self.storage[max_child_index]

        self._sift_down(max_child_index)
