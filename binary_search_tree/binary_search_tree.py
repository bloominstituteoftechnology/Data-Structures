class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    element=self
    while True:
      if value<element.value:
        if element.left is None:
          element.left=BinarySearchTree(value)
          break
        else:
          element=element.left
      else: 
        if element.right is None:
          element.right=BinarySearchTree(value)
          break
        else:
          element=element.right


  def contains(self, target):
    element=self
    while True:
      if element.value==target:
        return True
      elif target<element.value:
        if element.left is not None:
           element=element.left
        else:
          return False
      else:
        if element.right is not None:
          element=element.right
        else:
          return False

  def get_max(self):
    element=self
    while True:
      if element.right is not None:
        element=element.right
      else:
        return element.value
