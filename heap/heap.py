class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    self.storage.append(value)
    self.count += 1
    parent = self.storage[self._get_parent(self.count -1 )]
    if parent > 0:
      left_val = self.storage[self._get_lefty(self.count - 1)]
      right_val = self.storage[self.get_righty(self.count - 1)]
      if self.storage[left_val] > self.storage[parent]
      
    # need to write a bubble up function to put element in place
    pass

  def delete(self):

    pass

  def get_max(self):
    return self.storage[0]
    pass

  def get_size(self):
    return self.count - 1
    pass

  def _get_parent(self, index):
    return (index - 1) // 2
    pass
  
  def _get_lefty(self, index):
    # these will be ODD index numbers
    lefty = (index * 2) + 1
    if lefty > len(self.storage) - 1:
      return None
    else:
      return lefty

  def _get_righty(self, index):
    # these will be EVEN index numbers
    righty = (index * 2) + 2
    if righty > len(self.storage) - 1:
      return None
    else:
      return righty

  def _bubble_up(self, index):
    
    left_val = self.storage[self._get_lefty(index - 1)]
    right_val = self.storage[self._get_righty(index - 1)]
    if left_val == None:
    if 
    pass

  def _sift_down(self, index):
    pass
