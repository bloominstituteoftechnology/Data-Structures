class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value, leaf=self.value):
        if leaf is not None:
            if value > leaf:
                # go right
                if self.right is None:
                    self.right = BinarySearchTree(value)
                    return value
                else:
                  # make self.right new value, and recall insert
                    new_value = self.right
                    BinarySearchTree.insert(value, new_value)
            else:
                # go left
                if self.left is None:
                    self.left = BinarySearchTree(value)
                    return value
                else:
                    # make self.left new value, and recall insert
                    new_value = self.left
                    BinarySearchTree.insert(value, new_value)
        else:
            self.value = BinarySearchTree(value)
            return value

    def contains(self, target, leaf=self.value):
        if leaf is not None:
            if target > leaf:
                  # if target is greater than leaf, go right
                leaf = self.right
                BinarySearchTree.contains(target, leaf)
            elif target < leaf:
                # target is less than leaf
                leaf = self.left
                BinarySearchTree.contains(target, leaf)
            else:
                # target is == leaf
                if target == leaf:
                    return leaf
                else:
                    return None

    def get_max(self, leaf=self.right):
        if leaf is not None:
            # if the leaf (self.right) is not none, make it new leaf and recheck
            leaf = self.right
            BinarySearchTree.get_max(leaf)
        else:
            # there is no more to the right, return current leaf
            return leaf
