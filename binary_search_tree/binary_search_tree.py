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
                    insert(self.right, value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    insert(self.left, value) 
  
    def contains(self, target):
        pass
  
    def get_max(self):
        pass
