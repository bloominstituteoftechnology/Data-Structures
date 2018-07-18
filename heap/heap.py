class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # append the value to self.storage
    self.storage.append(value)
    # increment the size
    self.size += 1

    #call bubble up to put value in a valid spot in the heap
    self._bubble_up(self.size) #where self.size is where the value was just appended

  def delete(self):
    #store max value in a variable so we can call it later
    returnvalue = self.storage[1]
    #replace the first storage element with the last element in the heap
    self.storage[1] = self.storage[self.size] #where self.size is the index of the last item in storage array
    self.size -= 1
    #remove the last element from the heap
    self.storage.pop()
    #call sift down to move the element at index 1 down to a valid spot in the heap
    self._sift_down(1)
    return returnvalue

  def get_max(self):
    return self.storage(1)

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # keep bubbling the element at the given index up the heap until it reaches a valid spot
    while index // 2 > 0:
      #loop until we no longer have a valid parent index
      #check to see if the element's parent's value < curr element's value
      if self.storage[index // 2] < self.storage[index]:
        #SWAP!
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      #update index value to parent's index
      # our heap element has reached valid spot
      else: 
        break #breaks out of loop
      index = index // 2 #will kick in next iteration of while loop

  def _sift_down(self, index):
    # keep sifting the element at the given index down the heap until it reaches a valid spot
    while (index * 2) <= self.size:
      # figure out which child is larger
      maxchild = self._max_child(index)
      # check to see if maxchild and current node need to be swapped
      if self.storage[index] < self.storage[maxchild]:
        #swap!
        self.storage[index], self.storage[maxchild] = self.storage[maxchild], self.storage[index]
      else:
        break
      index = maxchild

  def _max_child(index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      #return the child with the larger value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1