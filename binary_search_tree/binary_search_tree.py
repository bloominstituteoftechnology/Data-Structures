### Binary Search Trees
'''* Should have the methods `insert`, `contains`, `get_max`.
  * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
  * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  * `get_max` returns the maximum value in the binary search tree.
  * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 

'''

class BinarySearchTree:
  def __init__(self, value):
  # the value at th eurrent node
    self.value = value
    # reference to this node's left child
    self.left = None
    # reference to this node's right child
    self.right = None

  def insert(self, value):
    # check if the new node's value is less than
      # is there a child? If not insert new node
      #  otherwise repeat the process
    # check if new node's value is greater than
      # is there a child? if not insert new node
      # otherwise repeat the process
    if value < self.value:
        if not self.left:
            self.left = BinarySearchTree(value)
        else:
            # recursion call
            self.left.insert(value)
    else:
        if not self.right:
            self.right = BinarySearchTree(value) 
        else:
            self.right.insert(value)  

  def contains(self, target):
    if target == self.value:
      return True
    elif self.right is None and self.left:
      return False
    else:
      if self.left:
        if self.left.contains(target):
          return True
      if self.right:
        if self.right.contains(target):
          return True

  def get_max(self):
    while self.right is None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    if self.left:
      self.left.for_each(cb)
    cb(self.value)
    if self.right:
      self.right.for_each(cb)
    pass