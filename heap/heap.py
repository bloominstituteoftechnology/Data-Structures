import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage = self.storage + [value]
    self._bubble_up()

  def delete(self):
    return self._sift_down()

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self):
    for idx, val in enumerate(self.storage):

      at_left = False
      left_child_val = 2 * idx + 1
      right_child_val = 2 * idx + 2
      parent_val = math.floor((idx - 1) / 2)

      parent = ''
      left_child = ''
      right_child = ''

      if parent_val != -1:
        parent = self.storage[parent_val]
      else:
        parent = "top node"

      if left_child_val > len(self.storage) - 1:
        left_child = "out of range"
      else: 
        left_child = self.storage[left_child_val]

      if right_child_val > len(self.storage) - 1:
        right_child = "out of range"
      else:
        right_child = self.storage[right_child_val]

      if left_child != "out of range" and right_child == "out of range":
        if val < left_child:
          self.storage[idx] = left_child
          self.storage[left_child_val] = val


      elif left_child != "out of range" and right_child != "out of range":

        #compare left and right children see who is bigger
        if left_child > right_child:
          at_left = True

        if at_left == True:
          if val < left_child:
            self.storage[idx] = left_child
            self.storage[left_child_val] = val
        else:
          if val < right_child:
            self.storage[idx] = right_child
            self.storage[right_child_val] = val

  def _sift_down(self):
    if len(self.storage) == 1:
      first = self.storage[0]
      self.storage.pop(0)
      return first
    else:
      last = self.storage[len(self.storage) - 1]
      first = self.storage[0]
      self.storage.pop(0)
      self.storage.pop(len(self.storage) - 1)
      self.insert(last)
      return first
