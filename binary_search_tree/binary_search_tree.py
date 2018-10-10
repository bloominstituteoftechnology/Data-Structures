class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value <= self.value:
      if self.left:
        self.insert(self.left, value) 
      else:
        self.left = value
    else:
      if self.right:
        self.insert(self.right, value) 
      else:
        self.right = value

  def contains(self, target):
    if target == self.value:
      return True
    elif target <= self.value:
      self.contains(self.left, target)
    elif target > self.value:
      self.contains(self.right, target)
    else:
      return False

  def get_max(self):
    temp_array = []

    if self.left is None:
      temp_array.append(self.value)

    if self.right is None:
      temp_array.append(self.value)

    return self.get_max(self.left) + self.get_max(self.right)
