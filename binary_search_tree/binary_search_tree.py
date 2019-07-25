class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
          #search the left side for node placement
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
          #search the right side 
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
      #search the tree to see if new node is already in tree
        if target == self.value:
            return True
        elif self.right is None and self.left is None:
            return False
        else:
            if self.left is not None:
                if self.left.contains(target):
                    return True
            if self.right is not None:
                if self.right.contains(target):
                    return True

    def get_max(self):
      #Make sure the root node has the highest value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
