class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if self.value > value:
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.left and self.left.contains(target):
            return True
        elif self.right and self.right.contains(target):
            return True
        else:
            return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value
