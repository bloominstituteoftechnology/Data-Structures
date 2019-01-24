class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Why can I not reference self in start?
    def insert(self, value, start=self.value):
        if start is not None:
            # Moves it to the right if value is larger
            if value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                    return value
                else:
                    BinarySearchTree.insert(value, self.right)
            # Moves to the left
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                    return value
                else:
                    BinarySearchTree.insert(value, self.left)
        else:
            self.value = BinarySearchTree(value)
            return value

    def contains(self, target):
        pass

    def get_max(self):
        temp = self.right
        if self.right is not None:
            BinarySearchTree.get_max(self.right)
        else:
            return temp
