class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = BinarySearchTree(value)
    while self.value is not None:
      if self.value > value:
        if self.left == None:
          self.left = BinarySearchTree(value)
          return
        else:
          self.left.insert(value)
          return
      else:
        if self.right == None:
          self.right = BinarySearchTree(value)
          return
        else:
          self.right.insert(value)
          return
    
  def contains(self, target):
    if self.value == target:
      return True
    elif self.value > target:
      if self.left == None:
        return False
      elif self.left.value == target:
        return True
      else:
        self.left.contains(target)
    elif self.value < target:
      if self.right == None:
        return False
      elif self.right.value == target:
        return True
      else:
        self.right.contains(target)
    pass

  def get_max(self):
    # i tried to write this a different way, but nothing beats the way it was written by
    # my peer during the peer code review.
    # had to reuse it
    while self.right is not None:
      self = self.right
    return self.value
    pass
