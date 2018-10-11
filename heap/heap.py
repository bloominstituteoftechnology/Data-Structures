class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # if len(self.storage) <= 1:
    #   self.storage.append(value)
    # else: 
      self.storage.append(value)
      self._bubble_up(len(self.storage)-1)
      print(self.storage)
    

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    #index is the index of the element that will bemoving up the heap 
    #keep bubbling the element at the given index up the heap until it reachs a va...
    while (index-1) // 2 >= 0:
      if self.storage[(index-1)//2] < self.storage[index]:
      #swap the values
        self.storage[index], self.storage[(index-1) // 2] = self.storage[(index -1) // 2], self.storage[index]
      #update the index to be the parent's indes so that we can continte moving up the heap
      index = (index -1) // 2

  def _sift_down(self, index):
    pass
