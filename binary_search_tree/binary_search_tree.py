class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # this implementation doesn't balance itself or allow duplicates
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                # new leaf
                self.left = BinarySearchTree(value)
            else:
                # keep going
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                # new leaf
                self.right = BinarySearchTree(value)
            else:
                # keep going
                self.right.insert(value)

    def contains(self, target):
        if self.value is target:
            return True

        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
