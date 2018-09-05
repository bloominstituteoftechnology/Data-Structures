class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        newBST = BinarySearchTree(value)
        if value >= self.value:
            if self.right is None:
                self.right = newBST
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = newBST
            else:
                self.left.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        max = self.value
        if self.right:
            if self.right.value > max:
                return self.right.get_max()
        return max
