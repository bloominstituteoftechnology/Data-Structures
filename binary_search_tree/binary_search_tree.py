class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        direction = 'right' if value > self.value else 'left'
        if getattr(self, direction) is not None:
            self = getattr(self, direction)
        else:
            setattr(self, direction, BinarySearchTree(value))
            return value
        return self.insert(value)

    def contains(self, value):
        direction = 'right' if value > self.value else 'left'
        if self.value is not None and self.value != value and getattr(self, direction) is not None:
            self = getattr(self, direction)
        elif self.value is not None and self.value == value:
            return True
        else:
            return False
        return self.contains(value)


    def get_max(self):
        temp = self.right
        if self.right is not None:
            BinarySearchTree.get_max(self.right)
        else:
            return temp