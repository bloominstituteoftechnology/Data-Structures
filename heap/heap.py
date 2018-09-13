class Heap:
  def __init__(self):
    self.storage = []

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



  def insert(self, value):
    self.storage.append(value)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass



heap1 = Heap()
heap1.insert(5)
print(heap1.storage)