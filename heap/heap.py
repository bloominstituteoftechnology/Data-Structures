class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    #repalce the 1st storage elem with the last elem in the heap
    self.storage[0] = self.storage[-1]
    #remove the last elem in heap
    self.storage.pop()
    self._sift_down(0)
    return retval

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
#index is the index of the element that will be moving up the heap
#keep bubbling the element at the given index up the heap until it reaches a valid spot
    while (index - 1) // 2 >= 0:
#check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        #swap the values
        self.storage[index], self.storage[(index - 1 ) // 2] = self.storage[(index - 1) // 2], self.storage[index]
#update the index to be the parent's index so that we can continue moving up the heap
      index = (index - 1) // 2

  def _sift_down(self, index):
#as long as left index is in bound of total indices we keep moving
    while index * 2 + 1 <= len(self.storage) - 1:
#figure out the larger of the 2 children, assuming there are 2
  #create a function and define it below
  #this function receives the index, look at the children of that index
  #then return the index of the higher priority
      maxChild = self._max_child(index)
#check to see if we need to swap
      if self.storage[index] < self.storage[maxChild]:
        self.storage[index], self.storage[maxChild] = self.storage[maxChild], self.storage[index]
#then update the index
      index = maxChild

#DEFINE THE MAXCHILD FUNCTION FROM ABOVE
  def _max_child(self, index):
#check if the right child index is out of bounds of storage array
#we check the right side because
    if index * 2 + 2 > len(self.storage) - 1:
      #return the left child index
      return index * 2 + 1
    else:
#return the index connected to the child node that has the larger value
#THIS IS A PYTHON TERNARY
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2