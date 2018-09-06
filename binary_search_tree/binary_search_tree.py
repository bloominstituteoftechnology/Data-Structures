class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        newTree = BinarySearchTree(value)
        if self.value > value:
            if not self.left:
                self.left = newTree
            else:
                self.left.insert(newTree)
        else:
            if not self.right:
                self.right = newTree
            else:
                self.right.insert(newTree)

    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right and self.right.contains(target):
                return True
        else:
            if self.left and self.left.contains(target):
                return True

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value
