class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):    
    # insert value to the very end of the storage list
    self.storage.append(value)
    # if pre-insertion storage size was at least 1:
    storage_size = self.get_size()
    if storage_size != 0:  
      current_index = storage_size-1
      while current_index >= 0:
        self._bubble_up(current_index)
        # update current_index to its parent's index
        if current_index % 2 == 0:
          current_index = int((current_index - 2) / 2)
        else:
          current_index = int((current_index - 1) / 2)

  def delete(self):
    self.storage.pop(0)
    current_index = 0
    while current_index < self.get_size():
      self._sift_down(0)
      current_index += 1

  def get_max(self):
    if len(self.storage) == 0:
      return 0
    else:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # only do something when storage size is greater than 1, since for size 1, root has no parent node to compare with
    if self.get_size() > 1:
      # if index is to the left of its parent in the heap, set parent index
      if index % 2 == 1:
        parent_index = int((index-1) / 2)  
      # if index is to the right of its parent in the heap, set parent index
      else:
        parent_index = int((index-2) / 2)
      # if parent is smaller than value of index, perform value swap
      if parent_index >= 0:
        if self.storage[parent_index] < self.storage[index]:
            parent_value = self.storage[parent_index]
            self.storage[parent_index] = self.storage[index]
            self.storage[index] = parent_value

  def _sift_down(self, index):
    # obtain values of each child and the higher of the two children
    left_child = self.storage[(2*index)+1]
    right_child = self.storage[(2*index)+2]
    max_child = max(left_child, right_child)
    current_value = self.storage[index]
    # if one of the children is greater than value of index, find which child is the greater, and perform swap with index
    if max_child > current_value:
      if left_child >= right_child:
        self.storage[index] = left_child
        self.storage[(2*index)+1] = current_value
      else:
        self.storage[index] = right_child
        self.storage[(2*index)+2] = current_value
      





