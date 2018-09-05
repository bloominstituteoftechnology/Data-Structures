import math

def swap( arr, a, b ):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp
  return arr

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # add to array
    self.storage.append( value )
    # bubble up
    self._bubble_up( self.size + 1 )
    # update size
    self.size += 1

  def delete(self):
    # SAVE VALUE to return
    val = self.storage[1]
    # swap first and last element
    self.storage[1] = self.storage[self.size]
    self.storage.pop()
    # update size
    self.size -= 1
    # sift down
    self._sift_down(1)
    # return val
    return val

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # if node smaller than parent
    if index <= 1 or self.storage[index] <= self.storage[(math.floor(index/2))]:
      return None
    # while node > it's parent
    else:
      # swap parent & value @ index
      temp = self.storage[index]
      self.storage[index] = self.storage[(math.floor(index/2))]
      self.storage[(math.floor(index/2))] = temp
      # recursive call
      return self._bubble_up((math.floor(index/2)))

  def _sift_down(self, index):
    # Compare the new root with its children; if they are in the correct place return None
    print( self.storage )
    left = 2*index
    right = 2*index+1
    print( str(index) + " " + str(left) + " " + str(right) )
    # bounds check
    if left <= self.size:
      if self.storage[left] > self.storage[index]:
        # bounds check
        if right <= self.size:
          if self.storage[right] > self.storage[index]:
            # sift down with max child
            if self.storage[right] > self.storage[left]:
              self.storage = swap( self.storage, index, right )
              return self._sift_down( right )
            # no right child, sift down left
            else:
              self.storage = swap( self.storage, index, left )
              return self._sift_down( left )
        self.storage = swap( self.storage, index, left )
        return self._sift_down( left )
    return None
  