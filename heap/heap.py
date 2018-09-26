class Heap:


# The key is stored in the array representation of the tree (i.e. self.storage) 
# such that its index is equal to the level number f(key) of key defined as follows:
#         *If key = root of tree, then f(p) = 0
#         *If key is the left child of key q, then f(p) = 2 * f(q) + 1
#         *If key is the right child of key q, then f(p) = 2 * f(q) + 2

#So, let's say we have the following heap:
#           2
#     4          8
#  17   21    23   28

# f(2) = 0 (top level)
# f(4) = 2 *  f(2) + 1 = 1
# f(8) = 2 * f(2) + 2 = 2
# f(17) = 2 * f(4) + 1 = 3
# f(21) = 2 * f(4) + 2 = 4
# f(23) = 2 * f(8) + 1 = 5
# f(28) = 2 * f(8) + 2 = 6

#The above then implies that the heap would be stored in storage as follows:
# storage = [2 4 8 17 21 23  28]

# Put in another way, the index of root element is storage[0], and the index of the 
# the nodes relating to the i'th node is as follows:
#       Parent      = storage[(i-1)/2] 
#       Left Child  = storage[(2*i) + 1]
#       Right Child = storage[(2*i)+ 2]


# ### Heaps
# * Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
#   * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
#   * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
#   * `get_max` returns the maximum value in the heap _in constant time_.
#   * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
#   * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    oldTop = self.storage[0]
    newTop = self.storage[len(self.storage)-1]
    self.storage[0] = newTop
    self.storage.pop()
    self._sift_down(0)
    return oldTop

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)


# Put in another way, the index of root element is storage[0], and the index of the 
# the nodes relating to the i'th node is as follows:
#       Parent      = storage[(i-1)/2] 
#       Left Child  = storage[(2*i) + 1]
#       Right Child = storage[(2*i)+ 2]

  def _bubble_up(self, index):
    if index == 0:
      pass
    
    while index > 0:
      value = self.storage[index]
      parent = self.storage[(index-1)//2]
      
      if parent < value:
        self.storage[index] = parent
        self.storage[(index-1)//2] = value
      
      index = (index-1)//2


  def _sift_down(self, index):

    while (2*index+2) < len(self.storage)-1:
      value = self.storage[index]
      left_child = self.storage[(2*index)+1]
      right_child = self.storage[(2*index)+2]

      if value < left_child:
        if right_child>left_child:
          self.storage[index] = right_child
          self.storage[(2*index)+2] = value
        
        if left_child>right_child:
          self.storage[index] = left_child
          self.storage[(2*index)+1] = value
        
        index = 2*index + 1
        



heap1 = Heap()
heap1.insert(5)
heap1.insert(6)
heap1.insert(7)
heap1.insert(8)
heap1.insert(4)
heap1.insert(100)
heap1.insert(101)
print(heap1.storage)
heap1.delete()
print(heap1.storage)