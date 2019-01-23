class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        attr = "right" if value >= self.value else "left"
        child_bst = getattr(self, attr)
        if child_bst is None:
            new_bst = BinarySearchTree(value)
            setattr(self, attr, new_bst)
        else:
            child_bst.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        attr = "right" if target > self.value else "left"
        child_bst = getattr(self, attr)
        if child_bst is None:
            return False
        return child_bst.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
