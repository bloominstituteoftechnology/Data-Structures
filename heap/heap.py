class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    storage = self.storage
    if storage == []:
      return storage.append(value)

    lastIndex = storage.index(storage[-1])
    storage.append(value)

    if len(storage) == 1:
      return storage
    
    return self._bubble_up(lastIndex) 

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    storage = self.storage
    parentIndex = (index - 1) // 2
    if index <= 0 or parentIndex < 0:
      return 
    elif storage[parentIndex] < storage[index]:
      storage[index], storage[parentIndex] = storage[parentIndex], storage[index]
      index = parentIndex
      
    return self._bubble_up(index) 
    
  def _sift_down(self, index):
    storage = self.storage
    left = (2 * index) + 1
    right = (2 * index) + 2
    
    if left is not None:
      index = left
      return _sift_down(index)
    elif right is not None: 
      index = right
      return _sift_down(index)
    elif left is None:   
      storage[left] = storage[index]
    elif right is None:
      storage[right] = storage[index]  
    
      
    