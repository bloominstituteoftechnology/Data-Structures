class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(self, value):
    # need a recursive function that movs along the tree and inserts a node where it belongs.
    # if value less than parent go down left branch
    if value < self.value:
        if self.left != None:
            self.left.insert(value)
        else:
            self.left = BinarySearchTree(value)

    elif value > self.value:
        # Same as before, but down the right branch for greater values
        if self.right != None:
            self.right.insert(value)
        else:
            self.right = BinarySearchTree(value)


def contains(self, target):
    pass


def get_max(self):
    pass


def for_each(self, cb):
    pass
