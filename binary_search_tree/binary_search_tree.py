class BinarySearchTree:
    def __init__(self, value):
        # Root
        self.value = value
        # Root of left sub-tree
        self.left = None
        # Root of right sub-tree
        self.right = None

    def insert(self, value):
        # exit insert if value already exists
        if value == self.value:
            return
        # If value is smaller
        elif self.value > value:
            if self.left is None:
                # Create a leaf
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        # If value is bigger
        elif self.value < value:
            if self.right is None:
                # Create a leaf
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # follow down the right ->
        # if at the end
        if self.right is None:
            # this is the biggest value
            return self.value
        else:
            # go deeper!
            return self.right.get_max()
