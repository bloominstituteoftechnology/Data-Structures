class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value, leaf=self.value):
        if value > leaf:
            # go right
            if self.right is None:
                self.right = value
            else:
                # make self.right new value, and recall insert
                new_value = self.right
                insert(value, new_value)
        else:
            # go left
            if self.left is None:
                self.left = value
            else:
                # make self.left new value, and recall insert
                new_value = self.left
                insert(value, new_value)

    def contains(self, target, leaf=self.value):
        if leaf is not None:
            if target > leaf:
                # if target is greater than leaf, go right
                leaf = self.right
                contains(target, leaf)
            elif target < leaf:
                # target is less than leaf
                leaf = self.left
                contains(target, leaf)
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
            get_max(leaf)
        else:
          # there is no more to the right, return current leaf
            return leaf
