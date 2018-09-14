class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
      if value < self.value:
        if self.left == None:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)
      elif value > self.value:
        if self.right == None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)
      else:
          self.value = value
        

    def contains(self, target):
      if self.value == target:
        return True
      elif target < self.value and self.left: 
        return self.left.contains(target)
      elif target > self.value and self.right:
        return self.right.contains(target)
      else:
        return False

    def get_max(self):
      
        pass


tree = BinarySearchTree(10)
print(tree.insert(20))
