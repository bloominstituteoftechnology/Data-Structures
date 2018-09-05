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
        pass


bst = BinarySearchTree(5)
# print(bst.contains(5))
bst.insert(7)
print(bst.contains(7))
# print(bst.right.value)
# bst.insert(8)
# print(bst.right.right.value)
# bst.insert(7)
# bst.insert(6)
# bst.left.right.value  # 3
# bst.right.left.value  # 6
