class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    #put the value at the end of the storage array
    self.storage.append(value)
    #call the bubbleUp helper method to move the value to a valid spot in heap
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    #init a variable to hold the element that is going to be deleted
    rv = self.storage[0]
    #replace the first storage element with the last element in heap and #remove the last element
    self.storage[0] = self.storage.pop()
    #call sift down to move the element at index 0 down to a valid spot
    self._sift_down(0)
    return rv

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    #in a while loop, keep bubbling the element at index up the heap
    while (index - 1) // 2 >= 0:
      #check if element's parent's value is less than current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        #if true swap both values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) //2]
      index = (index - 1) // 2

  def _sift_down(self, index):
    pass
