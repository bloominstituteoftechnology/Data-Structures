class Node:
    def __init__(self, value=None, L=None, R=None):
        self.value = value
        self.L = L
        self.R = R


class BinarySearchTree:
    def __init__(self, root=None, L = None, R = None):
        self.root = Node(root)
        self.L = L
        self.R = R

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.value > value:
            if node.L is None:
                node.L = Node(value)

            else:
                self._insert(node.L, value)
        else:
            if node.R is None:
                node.R = Node(value)
            else:
                self._insert(node.R, value)

    def contains(self, target):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if node.value == target:
                return True
            if target >= node.value:
                node = node.R
            else:
                node = node.L
        return False

    def get_max(self):
        if self.root is None:
            return None
        node = self.root
        while node.R is not None:
            node = node.R
        return node.value


# bt = BinarySearchTree(2)
# print(bt.root.value)
