class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    #stores value at the end of the list
    #compares new value to previous 
    # bubbles up if new value is greater than previous value
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    #delete is to delete the max number in heap
    #swaps index 0 with the last index if the len of list is more than 1
    # then sift down to make sure the new max is at top
    #if only one value in heap then just delete the value
    # if nothing in heap then return false
    if len(self.storage) > 1:
      self.swap(0,len(self.storage)-1)
      max = self.storage.pop()
      self._sift_down(0)
    elif len(self.storage) == 1:
      max = self.storage.pop()
    else:
      max = False
    return max

    

  def get_max(self):
    #max heap has max number at index 0, return index 0
    return self.storage[0]

  def get_size(self):
    # size is the number of elements in the list so return len of storage list
    return len(self.storage)

  def _bubble_up(self, index):
    #find parent index
    # check if index is the top already, return if it is
    # if index is great than parents , then swap the function
    parent = (index-1)// 2
    if index <= 0 :
      return
    elif self.storage[index] > self.storage[parent]:
      self.swap(index,parent)
      self._bubble_up(parent)

  def _sift_down(self, index):
    #compares values in the heap
    #swaps if top value to left or right depending on the largest value
    #recursive to make sure all the values are in the right spot
    left = (index * 2) + 1
    right = (index * 2) + 2
    max = index

    if len(self.storage) > left and self.storage[max] < self.storage[left]:
      max = left
    if len(self.storage) > right and self.storage[max] < self.storage[right]:
      max = right
    if max != index:
      self.swap(index, max)
      self._sift_down(max)
  
  #helper function to swap indices
  def swap (self,a,b):
    self.storage[a], self.storage[b] = self.storage[b], self.storage[a]

  #test passed

    
