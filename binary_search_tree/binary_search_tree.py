class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.value = BinarySearchTree(value)
            else:
                self.left.insert(BinarySearchTree)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left is None:
                return False
            elif target == self.value:
                return True
            else:
                return self.contains(target)

        elif target > self.value:
            if self.right is None:
                return False
            elif target == self.value:
                return True
            else:
                return self.contains(target)

    def get_max(self):
        right_branch = self.value if self.right is None else self.right.get_max()

        return max(self.value, right_branch)

    def for_each(self, cb):
        pass
