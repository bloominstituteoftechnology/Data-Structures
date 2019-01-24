class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value): #bubble up
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1) # storage index subtract 1

  def delete(self): #sift down
    # deletes from root
    # creates a vacant space thats filled by last element of array
    # sift that last element down
    if len(self.storage) == 0:
      return None

    max_deleted = self.storage[0] #saving deleted to a variable 
    self.storage[0] = self.storage[-1] #copies the last value into the first value
    self.storage.pop() #delete the max value which is at the end now
    self._sift_down(0) #swift down the 1st value to the right position
    return max_deleted
    
  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)
  

  def _bubble_up(self, index):
    index_of_parent = (index - 1) //2 
    if index == 0: #no parent
      return
    if self.storage[index_of_parent] < self.storage[index]:
      temp = self.storage[index_of_parent]
      self.storage[index_of_parent] = self.storage[index]
      self.storage[index] = temp
      self._bubble_up(index_of_parent)

  def _sift_down(self, index):
    index_left = 2 * index + 1
    index_right = 2 * index + 2
    index_of_child = index_left

    if self.get_size() - 1 < index_left: #all of the nodes no children
      return
    
    if self.get_size() - 1> index_left and self.get_size() > index_right: #both children
      if self.storage[index_left] < self.storage[index_right]:
        index_of_child = index_right
      # when childs value greater than parent value switch indexs(swap)
      if self.storage[index_of_child] > self.storage[index]:
        temp = self.storage[index]
        self.storage[index] = self.storage[index_of_child]
        self.storage[index_of_child] = temp
        self._sift_down(index_of_child)
    else: #only one child which we be the index_left
      if self.storage[index_left] > self.storage[index]:
        temp = self.storage[index]
        self.storage[index] = self.storage[index_left]
        self.storage[index_left] = temp
        return

     # self.storage[index], self.storage[index_of_child] = self.storage[index_of_child], self.storage[index]


#find parent index from child by doing index = (childIndex - 1) // 2
#parents children will be index(of the parent)
  # parentIndex * 2 + 1 left child
  # parentIndex * 2 + 2 right child