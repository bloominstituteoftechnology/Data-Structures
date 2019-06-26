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
    # takes target value and checks tree to see if that value already exists.
    if target < self.value:
        if self.left == None:
            return False
        return self.left.contains(target)

    # if value is greater than parent check right
    if target > self.value:
        if self.right == None:
            return False
        return self.right.contains(target)


def get_max(self):
    if self.right:
        return self.right.get_max()

    return self.value


def for_each(self, cb):
    cb(self.value)
    if self.left:
        self.leftfor_each(cb)
    if self.right:
        self.right.for_each(cb)    
