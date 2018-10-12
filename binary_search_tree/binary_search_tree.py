class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if not self.right:
                self.right=BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left=BinarySearchTree(value)
            else:
                self.left.insert(value)
             

    def contains(self, target):
        current = self
        element = False
        while (current and element!=True):
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            else:
                element = True
        return element

    def get_max(self):
        if self.right == None:
            return self.value
        return self.right.get_max()
