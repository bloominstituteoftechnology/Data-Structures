class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if new_value == self.value:
        return
    elif new_value < self.value:
        if self.left == None:
            self.left = BinarySearchTree(new_value)
        else:
            self.left.insert(new_value)
    else:
        if self.right == None:
            self.right = BinarySearchTree(new_value)
        else:
            self.right.insert(new_value)

  def contains(self, target):
    if value == self.value:
        return True
    elif value < self.value:
        if self.left:
            return self.left.__contains__(value)
        else:
            return False
    else:
        if self.right:
            return self.right.__contains__(value)
        else:
            return False

  def get_max(self):
    pass
