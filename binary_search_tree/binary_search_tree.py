class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        done = False
        current = self

        while not done:
            if value >= current.value:
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
        done = False
        current = self

        while not done:
            if target == current.value:
                return True

            if target >= current.value:
                if not current.right:
                    return False

                current = current.right
            else:
                if not current.left:
                    return False

                current = current.left

    def get_max(self):
        current_node = self
        next_node = current_node.right

        while current_node:
            if not next_node:
                return current_node.value
            
            current_node = next_node
            next_node = current_node.right