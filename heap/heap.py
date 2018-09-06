class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    if len(self.storage) == 0:
      self.storage.append(value)
      return
    
    self.storage.append(value)

    childIndex = len(self.storage) - 1
    parentIndex = self._bubble_up(childIndex)

    while self.storage[childIndex] > self.storage[parentIndex]:
      
      tempChild = self.storage[childIndex]
      self.storage[childIndex] = self.storage[parentIndex]

      self.storage[parentIndex] = tempChild

      childIndex = parentIndex
      parentIndex = self._bubble_up(childIndex)
      
      if childIndex == 1 and parentIndex == 0 and self.storage[childIndex] > self.storage[parentIndex]:
        tempChild = self.storage[childIndex]
        self.storage[childIndex] = self.storage[parentIndex]
        self.storage[parentIndex] = tempChild
        return
      if childIndex or parentIndex < 0:
        return
        


  def delete(self):
    poppedVal = self.storage.pop()
    self.storage[0] = poppedVal
    

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # Finds parent index of the child
    parentIndex = (index - 1) // 2
    return parentIndex

  def _sift_down(self, index):
    # Finds the child index of the parent
    childIndex = 0
    if index % 2 == 0:
      childIndex = 2 * index + 2
    else:
      childIndex = 2 * index + 1
    return childIndex

if __name__ == '__main__':
  heap = Heap()
  heap.insert(100)
  heap.insert(19)
  heap.insert(36)
  heap.insert(25)

  print(heap.storage)