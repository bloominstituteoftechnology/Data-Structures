class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    #if empty just insert item
    if len(self.storage) == 0:
      self.storage.append(value)
      self.count += 1
      parent = _get_parent(self.count -1) #off by one??? maybe?
      while parent < value: 
        self._bubble_up(self.count -1)
        parent = _get_parent(self.count -1) #off by one??? maybe not -1?
        
    #otherwise insert item to end and sift it up


  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    return self.count 

#underscore means private function for internal use only
  def _get_parent(self, index):
    return storage[(index-1)//2]

  def _get_left(self, index):
    left_index = index*2+1
    if left_index > len(self.storage) - 1:
      

  # def _get_right(self, index):
  #   return 

  def _get_left()

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
