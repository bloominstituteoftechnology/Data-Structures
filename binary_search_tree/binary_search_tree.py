class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
       self.value = BinarySearchTree(value)

    elif self.value > value:
        if self.left == None:
          self.left = BinarySearchTree(value)
        else:
          return self.left.insert(value)
          
    else:
        if self.right == None:
          self.right = BinarySearchTree(value)
        else:
          return self.right.insert(value)

  def contains(self, target):

    if self.value == target:
      return True

    elif self.left == None and self.right == None:
      return False

    elif self.value > target:
      return self.left.contains(target)

    else:
      return self.right.contains(target)

        
      
    

  def get_max(self):
    max_value = self.value

    if self.value == None:
      return max_value

    elif self.right != None:
      return self.right.get_max()
    
    else:
      return max_value
