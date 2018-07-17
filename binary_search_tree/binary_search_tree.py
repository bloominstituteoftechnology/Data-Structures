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
        max_value = self.value
        current = self
        next_node = self.right

        while current:
            if not current.right:
                print(current.value)
                return max_value

            if current.value > max_value:
                print(f"{current.value} is greater than {max_value}")
                return current.value
            
            current = next_node
