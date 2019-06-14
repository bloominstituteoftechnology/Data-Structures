class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        maxval = self.value
        if not self.right:
            return maxval
        return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
print(bst.contains(7))
