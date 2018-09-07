class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    current = self

    while current.value is not target:
      if current is not None:
        if target < current.value:
          current = current.left
        else:
          current = current.right
      
      if current is None:
        return False

    return True

  def get_max(self):
    current = self
    current_max = current.value

    while current is not None:
      if current.value >= current_max:
        current_max = current.value
        current = current.right
        
    return current_max
