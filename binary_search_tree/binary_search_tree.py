class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Check if the value being inserted is less than the node's current value.
    # If it is we go left.
    if value < self.value:
      # If there is no current Node in the left node
      if self.left is None:
        # Create one
        self.left = BinarySearchTree(value)
      else:
        # Otherwise recurse until we find one.
        self.left.insert(value)
    # If the value is greater or equal to the node's current value. We go right.
    else:
      # If there is no current Node in the right node
      if self.right is None:
        # Create a node on the right
        self.right = BinarySearchTree(value)
      else:
        # Else we recurse until we find one
        self.right.insert(value)
    
  def contains(self, target):
    # First we need to see if the current node contains the target value.
    # Else we need to check if it's lesser or greater than the current Node's value
    # Then we need to go either left (lesser) or right (greater)
    doesContain = False
    if target == self.value:
      return True
    else:
      # The target value is less than the current node's value. Go left.
      if target < self.value:
        # First check if there is a left node.
        # If there isn't a left node than we return False. This tree does not contain the target value.
        if self.left is None:
          return False
        else:
          # Recurse down the left path
          doesContain = self.left.contains(target)
      else:
        if self.right is None:
          return False
        else:
          # Recurse down the right path
          doesContain = self.right.contains(target)
    return doesContain

  def get_max(self):
    max = 0
    print(self.right is not None)
    if self.right is None:
      print('return value')
      return self.value
    else:
      while self.right is not None:
        max = self.right.get_max()
    return max

  def for_each(self, cb):
    pass