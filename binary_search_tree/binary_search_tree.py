class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        cb(self.value)
        if self.right:
            self.right.for_each(cb)


bst = BinarySearchTree(5)

bst.insert(2)
bst.insert(3)
bst.insert(7)

print(bst.contains(7))
