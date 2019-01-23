class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BinarySearchTree(value)

        def rec(target, current_node):
            if target > current_node.value:
                if current_node.right is None:
                    current_node.right = node
                    return
                else:
                    rec(target, current_node.right)
            elif target < current_node.value:
                if current_node.left is None:
                    current_node.left = node
                    return
                else:
                    rec(target, current_node.left)

        return rec(value, self)

    def contains(self, target):
        pass

    def get_max(self):
        pass


bst = BinarySearchTree(5)

bst.insert(2)

print(bst.left, bst.right)
