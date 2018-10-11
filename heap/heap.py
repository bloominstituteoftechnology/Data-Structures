class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass
    # storage = self.storage
    # if storage == []:
    #   return storage.append(value)

    # lastIndex = storage.index(storage[-1])
    # storage.append(value)

    # if len(storage) == 1:
    #   return storage
    
    # return self._bubble_up(lastIndex) 

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    storage = self.storage
    parentIndex = (index - 1) // 2
    while parentIndex >= 0:
      if storage[parentIndex] < storage[index]:
        tmp = storage[parentIndex]  
        storage[parentIndex] = storage[index]
        storage[index] = tmp
        index = parentIndex
      
  def _sift_down(self, index):
    pass
  #   storage = self.storage
  #   left = (2 * index) + 1
  #   right = (2 * index) + 2
    
  #   while left is not None:
  #     index = left
  #     self._sift_down(index)
  #   elif right is not None: 
  #     index = right
  #     return _sift_down(index)
  #   elif left is None:   
  #     storage[left] = storage[index]
  #   elif right is None:
  #     storage[right] = storage[index]  
    
      
    