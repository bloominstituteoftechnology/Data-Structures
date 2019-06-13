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

        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)

            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        elif self.left and target < self.value:
            return self.left.contains(target)

        elif self.right and target > self.value:
            return self.right.contains(target)

        else:
            return False

    def get_max(self):
        current = self
        while current:
            if not current.right:
                return current.value
            current = current.right
        return current.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


# to test solutions
bst = BinarySearchTree(5)
bst.insert(4)
bst.insert(5)
bst.insert(20)
bst.insert(11)
bst.insert(15)

print(bst)
print(bst.contains(11))
print(bst.get_max())
