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
        elif self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # if null create leaf
        # else insert(self.left.insert)

    def contains(self, target):
        # if target is == self.value return True
        # if target is > self.value check self.right
        # if target is < self.value check self.left
        # repeat
        pass

    def get_max(self):
        # follow down the right ->
        pass
