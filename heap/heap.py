class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):  # O(log(n))
      
    # The item is always inserted at the bottom
    # Bubble up
      # Then we check if the item has a parent and if it is bigger or smaller than its parent
      # If the item is bigger, then we swap them
      # Then we check again, until either the item is less than its parent or it no longer has a parent
    
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1) # O(log(n))

  def delete(self):  # O(log(n))
    
    ## More than 1 item?
    # Swap the maxValueToDelete with the last item in the tree
    # Delete the maxValueToDelete
    # sift the item down to where is belongs
      # Compare the item with its two children, and swap with the child that is the largest of the two children
      # Compare the item again with its new two children, if there are any
    ## Just 1 item?
    ## Empty heap?
    
    if len(self.storage) == 0:
      return None
    elif len(self.storage) == 1:
      return self.storage.pop()  # pop deletes and returns the value
    
    return_value = self.storage[0]  # max node
    self.storage[0] = self.storage[len(self.storage) - 1]  # grab last item and put it in the top
    self.storage.pop() # delete the last item, dont really care to put the max node in there before we delete
    self._sift_down(0)  # sift the top value down if needed  O(log(n))
    return return_value
   
  def get_max(self):  # O(1)
    
    # The max value is always the first node
    # Check if there is at least one node, then return the value
    
    if len(self.storage) > 0:
      return self.storage[0]

  def get_size(self): # O(1)
    
    return len(self.storage)

  def _bubble_up(self, index):  # O(log(n))
    
    parent = (index - 1) // 2
    
    # There is only 1 item
    if index < 1:
      return
    
    # If the item passed in is greater than the parent, then swap them, and bubble it up again if needed
    elif self.storage[index] > self.storage[parent]:
      self._swap(index, parent)  # O(1)
      self._bubble_up(parent)    # O(log(n))

  def _sift_down(self, index):      # O(log(n))
    
#    left_index = index * 2 + 1
#    right_index = index * 2 + 2
#    
#    largest = index
#
#    # Make sure the child exists then check if its bigger or smaller than the parent
#    # Determine the largest child
#    if len(self.storage) > left_index and self.storage[largest] < self.storage[left_index]:
#      largest = left_index
#    
#    if len(self.storage) > right_index and self.storage[largest] < self.storage[right_index]:
#      largest = right_index
#    
#    if largest != index:
#      self._swap(index, largest)
#      self._sift_down(largest)
#      
    
    while True:
      
      left_index = index * 2 + 1
      right_index = index * 2 + 2
 
      largest = index
      
      if len(self.storage) > left_index and self.storage[largest] < self.storage[left_index]:
        largest = left_index
      
      if len(self.storage) > right_index and self.storage[largest] < self.storage[right_index]:
        largest = right_index
        
      if largest == index:
        return
      
      self._swap(index, largest)
      index = largest  # reset the index to be the new child's index
      
      
    ## runtime complexity is O(log(n)) for both because its a tree
    ## space complexity of while loop is O(1) because the stuff inside is all O(1)
    ## space complexity of recursive function is O(log(n)) because  calling a function allocates more memory on the stack for every recursion, and because the method is log(n) the space complexity is at least that.
          
  def _swap(self, i, j):  # O(1)
    self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
# 