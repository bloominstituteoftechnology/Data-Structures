class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

    if value < self.value:
        self.right = BinarySearchTree(self.value)
        self.value = value
    else:
        self.left = BinarySearchTree(self.value)
        self.value = value
    print("value:", self.value, "left:", self.left, "right:", self.right)

  def contains(self, target):
    if self.value == target:
        return True
    if self.right != None and self.left != None:
        if self.right == target:
            return True
        elif self.left == target:
            return True
        else:
            self.contains(self.right, target)
            self.contains(self.left, target)

  def get_max(self):
    pass
