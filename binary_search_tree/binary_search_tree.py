class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
        if not self.right:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)
    else:
        if not self.left:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)

  def contains(self, target):
    if self.value == target:
        return True
    else:
        if self.value <= target:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        else:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
    # if target > self.value:
    # if self.right is not None: 
    #     return self.right.contains(targt)
    #     if target < self.value:
    #         if self.left is not None:
    #             return self.left.contains(target)
    #         if target == self.value:
    #             return True
    #     return False


  def get_max(self):
    if not self.right:
        return self.value
    return self.right.get_max()

    # *** V2 ***
    # current = root
    # while current.right:
    #     current = current.right
    # return current.value
