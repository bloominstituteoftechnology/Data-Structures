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

    if value < self.value:
      # If value is less, we go left.
      # If there is no left child, we park the node here
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else: self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif self.value > target:
      self.contains(self.right)
    elif self.value < target:
      self.contains(self.left)
    else:
      return False

  def get_max(self):
    cur_val = self.value
    # if cur_val <= self.right.value:
    #   cur_val = self.right.value

    if self.right is None:
      return self.value

    while self.right.value is not None:
      if cur_val <= self.right.value:
        cur_val = self.right.value
        self.get_max(self.right)
        return cur_val



  def for_each(self, cb):
    if self.left is None and self.right is None:
      cb(self.value)
    while self.left is not None or self.right is not None:
      if self.left:
        self.for_each(self.left)
      if self.right:
        self.for_each(self.right)