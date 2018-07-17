class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        parent = None
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        current = BinarySearchTree(value)

        if value < parent.value:
            parent.left = current
        else:
            parent.right = current

    def contains(self, target):
        current = self
        while current:
            if target == current.value:
                return True
            elif target < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value
