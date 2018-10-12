class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Adds input value to BST, left nodes smaller right increasing
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
    # Otherwise insert right since self.value is greater:
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # Return true if target = value in BST:
        if self.value == target:
            return True
        # Search Left is smaller than this node:
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Search Right is larger:
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # to look for a max value just keeping looking right
        if self.right:
            return self.right.get_max()
        return self.value
