class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # Append the value to the storage array.
    self.storage.append(value)
    # Increment the size.
    self.size += 1
    # Call the _bubble_up helper method to put this valid spot in the...
    self._bubble_up(self.size)

  def delete(self):
    # Store our max value in a variable so we can return it later.
    retval = self.storage[1]
    # Replace the first storage element with the last element in the heap.
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # Remove the last item from the heap.
    self.storage.pop()
    # Call _sift_down to move the element at index 1 down to a valid spot in the heap.
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # Keep bubbling the element at the given index up the heap until it reaches a valid spot.
    # By dividing the index by 2, you will get the parent index.
    # Loop until we no longer have a valid parent index (meaning a positive value)
    # We are using the indexing formula to grab it's parent
    while index // 2 > 0:
      # Check to see if the element's parent's value is less than the current value.
      if self.storage[index // 2] < self.storage[index]:
        # We need to swap them
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      # Our heap element has reached a valid spot in the heap.
      else:
        break
      # Update our index value to be the parent's index so that we can continue moving up the heap.
      index = index // 2

  def _sift_down(self, index):
    # Keep sifting the element at the given index down the heap until it reaches a valid spot.
    # We do index * 2 to find the index of its children.
    while (index * 2) <= self.size:
      # Figure out which child is larger
      mc = self._max_child(index)
      # Check to see if mc and the current node need to be swapped.
      if self.storage[index] < self.storage[mc]:
        # If it is, swap them.
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      else:
        break
      # Update our index value.
      index = mc

  def _max_child(self, index):
    # Right child
    if index * 2 + 1 > self.size:
      # Left child
      return index * 2
    else:
      # Return the child with the larger value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1