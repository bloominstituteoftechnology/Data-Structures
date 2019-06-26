class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  #we did this one in class
  #insert adds the input value to the binary search tree, 
  #adhering to the rules of the ordering of elements in a binary search tree
  def insert(self, value):
    if value < self.value:
            #let's check if there's a value there
        if not self.left:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)

    elif value >= self.value:
        if not self.right:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)


  #contains searches the binary search tree for the input value, 
  #returning a boolean indicating whether the value exists in the tree or not.
  def contains(self, target):
    #If the current value doesn't exist, return False
    if self.value is None:
      return False

    #If the current value is equal to the target
    if self.value == target:
      return True

    #If target is less than the current value, move to the left
    elif target < self.value:
      self.left
      #If the value is the target, return True
      if self.value == target:
        return True

      elif self.left is None:
        return False

      #Move to the left, if there is a node there, by calling this function again, 
      #but this time calling it on the left node
      elif self.left is not None:
        #Search, comparing the target with the current value again -- recursion
        return self.left.contains(target)

      elif self.left is None:
        #If you can't move further left, return False
        return False

    #If target is greater than or equal to the current value, move to the right
    elif target >= self.value:

      #If the value is the target, return True
      if self.value == target:
        return True

      if self.right is None:
        return False

      #Move to the right, if there is a node there, by calling this function again, 
      #but this time, calling it on the right node
      elif self.right is not None:
        return self.right.contains(target)

      elif self.right is None:
        return False

  #get_max returns the maximum value in the binary search tree
  def get_max(self):
    if self.right:
      self.right.get_max()
    else:
      return self.value

  #for_each performs a traversal of every node in the tree, 
  # executing the passed-in callback function on each tree node value. 
  # There is a myriad of ways to perform tree traversal; in this case any of them should work.
  #cb = callback just a function
  def for_each(self, cb):
    #I want to go through each node on the right and each node on the left
    if self.right:
        self.right.for_each(cb)
    if self.left:
        self.left.for_each(cb)