class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value, leaf=None):
        leaf = leaf if leaf is not None else self.value
        if value > leaf:
            # go right
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
              # make self.right new value, and recall insert
                new_leaf = self.right.value
                self.right.insert(value, new_leaf)
        else:
            # go left
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # make self.left new value, and recall insert

                new_leaf = self.left.value
                self.left.insert(value, new_leaf)
    # contains works in a seperate terminal, not in VSC for some reason

    def contains(self, target, leaf=None):
        leaf = leaf if leaf is not None else self.value
        print("current leaf is: ", leaf)
        print("we are looking for: ", target)
        if leaf is not None:
            if target > leaf:
              # if target is greater than leaf, go right
                leaf = self.right.value
                self.contains(target, leaf)
            elif target < leaf:
                # target is less than leaf
                leaf = self.left.value
                self.contains(target, leaf)
            else:
                if target == leaf:
                    print("we have a winner: ", leaf)
                    return True

                else:
                    return False
        else:
            return False

    def get_max(self, leaf=None):
        leaf = leaf if leaf is not None else self.value
        if self.right is not None:
            leaf = self.right.value
            self.get_max(leaf)
        else:
            return leaf
