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
        pass
  
    def get_max(self):
        max = self.value
        if self.right:
            if self.right.value > max:
                return self.right.get_max()
        return max
