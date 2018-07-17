class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if value is less than current value, check the left branch of the tree
        if value < self.value:
            # if the left branch is empty, create a BinarySearchTree with the argument's value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # if the left branch is not empty
                # call this function recursively on the left branch with the value
                self.left.insert(value)
        else:
            # if the right branch is empty, create a BinarySearchTree with the argument's value
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # if the right branch is not empty
                # call this function recursively on the right branch with the value
                self.right.insert(value)

    def contains(self, target):
        # if the target equals the current value, return True
        if target == self.value:
            return True
        # if the target is greater than the current value, check the right branch of the tree
        elif target > self.value:
            # if the right branch of the tree is empty, return False
            if self.right is None:
                return False
            # if the right branch of the tree is not empty,
            # call this function recursively on the right branch
            else:
                return self.right.contains(target)
        # if the target is not greater than the current value, check the left branch of the tree
        else:
            # if the left branch is empty, return False
            if self.left is None:
                return False
            # if the left branch of the tree is not empty,
            # call this function recursively on the left branch
            else:
                return self.left.contains(target)

    def get_max(self):
        # if the right branch is empty, return the current value
        if self.right is None:
            return self.value
        # if the right branch is not empty, call this function recursively on the right branch
        else:
            return self.right.get_max()
