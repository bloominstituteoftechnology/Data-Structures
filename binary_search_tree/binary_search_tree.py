class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        newTree = BinarySearchTree(value)
        if value < self.value:
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
        print('self.value is: {}'.format(self.value))
        print('self.target is: {}'.format(target))
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
        """ Non-recursive:
            max_value = self.value
            current = self
            while current:
                if current.value > max-value:
                    max_value = current.value
                current = current.right
            return max_value
        """
