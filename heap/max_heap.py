class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) - 1
    self._bubble_up(index)


  def delete(self):
      max = self.storage[0]
      self.storage[0] = self.storage[-1]
      self.storage.pop()
      self._sift_down(0)
      return max



   # store what's at the front
   # put the smallest value at the front, then remove it from our storage
   # call sift down
   # return value

  def get_max(self):
   return  self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2
    while index >0 and self.storage[parent]<self.storage[index]:
        self.storage[parent],self.storage[index]=self.storage[index],self.storage[parent]
        index=parent
        parent = (index - 1) // 2
    ## while index greater than 0
    ## get the parent (index - 1) // 2
    ## if child is greater than parent--> comparator(child, parent)
    ## swap them
    ## if not, then we're still inside the while loop, but we have nothing to do
    ## break

  def _sift_down(self, index):
    # parent = (index - 1) // 2
    while index < len(self.storage)-1:
        #oick a child which is higher than the parent
        #if none are higher, then we are done
        #Find index of child1 and child2
        #Find higher child
        #Than compare parent with higher child
        #Swap if higher child is more than parent, else stop sift down
        left_child= 2*index+1
        right_child= 2*index+2
        lastIndex = len(self.storage)-1

        if left_child > lastIndex and right_child > lastIndex:
            return

        #one or both child are valid
        j = None

        if left_child <= lastIndex and right_child <= lastIndex:
            if self.storage[left_child] > self.storage[right_child]:
                j = left_child
            else:
                j = right_child

        elif left_child <= lastIndex:
            j = left_child
        else:
            j = right_child

        if self.storage[index] > self.storage[j]:
            return

        self.storage[index],self.storage[j] = self.storage[j] ,self.storage[index]
        index = j







