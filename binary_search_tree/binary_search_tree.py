class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Create a new instance for the new value to insert
        new_tree = BinarySearchTree(value)

        if value < self.value:
            # if there is no left child, set left child to new_tree
            if self.left is None:
                self.left = new_tree
            else:
                # else, repeat until left child is None
                self.left.insert(value)
        else:
            # if there is no right child, set right child to new_tree
            if self.right is None:
                self.right = new_tree
            else:
                # else, repeat until right child is None
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            # if self.left is not None
            if self.left:
                # keep searching...
                return self.left.contains(target)
        else:
            # if self.left is not None
            if self.right:
                # keep searching...
                return self.right.contains(target)

        return False

    def get_max(self):
        # recursively drill down on the right subtree
        # until you get the value of None.
        if self.right:
            return self.right.get_max()
        else:
            return self.value


bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(6)
bst.insert(7)
print(bst.get_max())
