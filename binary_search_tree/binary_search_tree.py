class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.value < value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value) 
  
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else: 
            if self.right:
                return self.right.contains(target)
            else:
                return False
  
    def get_max(self):
        max = self.value
        if self.right:
            if self.right.value > max:
                return self.right.get_max()
        return max
