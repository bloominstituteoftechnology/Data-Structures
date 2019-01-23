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
        def rec(value, current_node):
            if current_node is None:
                return False
            elif value == current_node.value:
                return True
            elif value > current_node.value:
                return rec(value, current_node.right)
            elif value < current_node.value:
                return rec(value, current_node.left)

        return rec(target, self)

    def get_max(self):
        maxValue = -float("inf")
        current_node = self
        while current_node is not None:
            if current_node.value > maxValue:
                maxValue = current_node.value
            current_node = current_node.right

        return maxValue


bst = BinarySearchTree(5)

bst.insert(2)
bst.insert(7)
bst.insert(4)
bst.insert(6)

print(bst.contains(4))
print(bst.contains(10))
