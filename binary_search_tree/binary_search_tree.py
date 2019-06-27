class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Wrap value in node.
    # 1. Compare the value against the current node value.
    # 2. Based on the result of the comparison, go left or right.
    # 3. If we find an empty spot, park the value there.
    # 4. Otherwise, repeat.
    # Base case: we've found an empty spot to park a value.

    if value > self.value:
      # If value is less, we go left.
      # If there is no left child, we park the node here
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass