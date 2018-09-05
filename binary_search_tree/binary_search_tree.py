class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_bst = BinarySearchTree(value)
        current = self
        put = False

        while put is False:
            if new_bst.value > current.value:
                if current.right is None:
                    current.right = new_bst
                    put = True
                else:
                    current = current.right
            elif new_bst.value < current.value:
                if current.left is None:
                    current.left = new_bst
                    put = True
                else:
                    current = current.left
            elif current.left is None and current.left is None:
                current = new_bst
                put = True

    def contains(self, target):
        current = self
        found = False
        while found is False:
            if current is None:
                break
            if target == current.value:
                found = True
            elif target > current.value:
                current = current.right
            elif target < current.value:
                current = current.left
        return found

    def get_max(self):
        current = self
        while current is not None:
            if current.right is None:
                return current.value
            else:
              current = current.right
