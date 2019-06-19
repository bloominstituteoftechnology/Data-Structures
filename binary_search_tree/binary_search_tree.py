class BinarySearchTree:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

  def insert(self, value):
      # Don't forget to wrap the value in a node
      # 1. Compare the element against the current node's value
      # 2. Based on the result of the comparison, go left or right
      # 3. If we find an empty spot, park the value there
      # 4. Otherwise, go back to step 1

      # What is the base case?
      # ------ Base case: We've found an empty spot where
      # ------ we can add the value
      if value < self.value:
          # If value is less, we go left
          # If there is no left child, we can park this node here
          if not self.left:
              # recurse on the left child
              self.left = BinarySearchTree(value)
          else:
              # insert on left
              self.left.insert(value)
      elif value >= self.value:
          if not self.right:
              # recurse on the right child
              self.right = BinarySearchTree(value)
          else:
              # insert on right
              self.right.insert(value)


  def contains(self, target):
      # we assume that tree doesn't contain target
      found_target = False
      # if target is root
      if target == self.value:
          found_target = True
      # if there's a node to the right
      # & target is greater than value there
      if self.right and target > self.value:
          found_target = self.right.contains(target)
      # if there's a node to the left
      # & target is less than value there
      if self.left and target < self.value:
          found_target = self.right.contains(target)
      return found_target
      

  def get_max(self):
      # we assume max_value is root node
      
      max_value = self.value
      # if no nodes on right then max_value is root
      if not self.right:
          return max_value
      # but if there are higher values than root
      # these will be on the right of root node
      # so we do the same steps as above recursively
      else:
          return self.right.get_max()


  def for_each(self, cb):
    cb(self.value)
    if self.right:
        self.right.for_each(cb)
    if self.left:
        self.left.for_each(cb)