class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):

        if target == self.value:
            return True
        elif target < self.value and self.left:
            if target == self.left.value:
                return True
            else:
                return self.left.contains(target)
        elif target > self.value and self.right:
            if target == self.right.value:
                return True
            else:
                return self.right.contains(target)

        return False

    def get_max(self):
        maxValue = self.value
        curr_node = self
        while (curr_node.right):
            curr_node = curr_node.right
            maxValue = curr_node.value

        return maxValue

    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)
