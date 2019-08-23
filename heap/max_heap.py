class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Check if storage is empty, if it is start at beginning
    # Put the value at the end of the list (append)
    # if Arr[i] > Arr[i/2] then swap (parent is bigger)
    if len(self.storage) == 0:
      self.storage.append(value)
    else:
      self.storage.append(value)
      last_index = len(self.storage) - 1
      if self.storage[last_index] > self.storage[last_index/2]:
        swap_value = self.storage[last_index]
        self.storage[last_index] = self.storage[last_index/2]
        self.storage[last_index/2] = swap_value

  def delete(self):
    # delete(): Deleting a key also takes O(Logn) time. We replace the 
    # key to be deleted with minum infinite by calling decreaseKey(). 
    # After decreaseKey(), the minus infinite value must reach root, 
    # so we call extractMin() to remove the key.
    pass

  def get_max(self):
    return self.storage[0] # Or 1 if you decide to do the 1 index method

  def get_size(self):
    # Traverse through and count all of the elements
    # This an array - len(self.storage)
    # For stretch practice, do this with a traversal similar to BST
    pass

  def _bubble_up(self, index):
    # Helper function to compare to parent node and switch if appropriate
    pass

  def _sift_down(self, index):
    pass