class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value:
            if value < self.value:
                if self.left is None:
                    return self.left = BinarySearchTree(value)
                else:
                    return self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    return self.right = BinarySearchTree(value)
                else:
                    return self.right.insert(value)
        else:
            return self.value = value

  def contains(self, target):
    if target < self.value:
            if self.left is None:
                return str(target)+" Not Found"
            return self.left.findval(target)
        elif target > self.value:
            if self.right is None:
                return str(target)+" Not Found"
            return self.right.findval(value)
        else:
            print(str(self.value)+ ' is found')

  def get_max(self):
    pass
