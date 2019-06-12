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
        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target < self.value:
            if target == self.left.value:
                return True
            elif not self.left.left or not self.left.right:
                return False
            else:
                self.left.contains(target)
        if target >= self.value:
            if target == self.right.value:
                return True
            elif not self.left.left or not self.left.right:
                return False
            else:
                self.right.contains(target)

    def get_max(self):
        if self.right:
            if self.right:
                return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)


bst = BinarySearchTree(5)

bst.get_max()
bst.insert(30)
bst.get_max()
bst.insert(300)
bst.insert(3)
bst.get_max(),
