class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.__bubble_up(self.size+1)
    self.size += 1
    

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
      if self.storate[index] < self.storage[(cieling(index-1)/2)]:
        return
      else:


  def _sift_down(self, index):
    
    pass
