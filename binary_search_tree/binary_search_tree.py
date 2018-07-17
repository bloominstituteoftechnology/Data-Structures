class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        done = False
        current = self

        while not done:
            if value > current.value:
                if not current.right:
                    current.right = BinarySearchTree(value)
                    break
                else:
                    current = current.right
            else:
                if not current.left:
                    current.left = BinarySearchTree(value)
                    break
                else:
                    current = current.left

    def contains(self, target):
        pass

    def get_max(self):
        pass
