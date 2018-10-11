class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    element=self
    while True:
      if value<element.value and element.left==None:
        element.left=BinarySearchTree(value)
        break
      elif value>element.value and element.right==None:
        element.right=BinarySearchTree(value)
        break
      elif value<element.value:
        element=element.left
      else:
        element=element.right


  def contains(self, target):
    pass

  def get_max(self):
    pass
