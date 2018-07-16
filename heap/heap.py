class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size = self.size + 1
    pass

  def delete(self):
    self.storage = self.storage[-1]
    pass

  def get_max(self):
    if len(self.storage) > 1:
      return self.storage[1]
    else:
        raise Exception
    pass

  def get_size(self):
    return 1
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
    
