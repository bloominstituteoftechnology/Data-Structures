class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # parent = floor(i-1/2)

  def delete(self):
    #left 2i+1 right 2i+2
    self.storage[0], self = self, self.storage[0]

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    #length of array

  def _bubble_up(self, index):
    

  def _sift_down(self, index):
    
