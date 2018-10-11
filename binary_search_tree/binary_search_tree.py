class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Check if value is less or greater then current value, if there something where it should go then it repeats this logic until it can become a leaf
    if value < self.value:
        if self.left == None:
            self.left = BinarySearchTree(value)
        else: self.left.insert(value)
    else:
        if self.right == None:
            self.right = BinarySearchTree(value)
        else: self.right.insert(value)

  def contains(self, target):
    # Similar logic to insert, keeps comparing target to values and works way down until it matches or runs out of nodes
    if target == self.value:
        return True
    else:
        if target < self.value:
            if self.left == None:
                return False
            else:
                 return self.left.contains(target)
        elif self.right == None:
            return False
        else:
            return self.right.contains(target)

  def get_max(self):
     # If there is no right value, then you know that number is the max
    if self.right == None:
        return self.value
    else:
        return self.right.get_max()
