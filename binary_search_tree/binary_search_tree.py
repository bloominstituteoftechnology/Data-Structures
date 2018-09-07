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
                self.left.insert(value)
        else:
            if not self.right:
                self.right = newTree
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
        else:
            if self.left:
                return self.left.contains(target)
        return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value
        # Non recursive method
        """ max_value = self.value
            current = self
            while current:
                if current.value > max-value:
                    max_value = current.value
                current = current.right
            return max_value
        """
