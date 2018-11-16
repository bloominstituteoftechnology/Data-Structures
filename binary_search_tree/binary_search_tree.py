class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, v):
        self.root = Node(v)
        self.max = v

    def get_root(self):
        return self.root

    def get_max(self):
        return self.max

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.max = value
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value > self.max:
            self.max = value

        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)

        if value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Entry already in BST")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left)
            print("Node: " + str(current_node.value))
            self._print_tree(current_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left, current_height + 1)
        right_height = self._height(current_node.right, current_height + 1)
        return max(left_height, right_height)

    def contains(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value is current_node.value:
            return True
        elif value < current_node.value and current_node.left is not None:
            return self._search(value, current_node.left)
        elif value > current_node.value and current_node.right is not None:
            return self._search(value, current_node.right)
        else:
            return False


def fill_tree(bst, n=100, max_int=100):
    from random import randint
    for _ in range(n):
        curr = randint(0, max_int)
        bst.insert(curr)
    return bst

tree = BinarySearchTree(5)
tree.insert(0)
tree.insert(3)
tree.insert(3)
tree.print_tree()
print(tree.get_root().left.right.value)
print(tree.get_max())
