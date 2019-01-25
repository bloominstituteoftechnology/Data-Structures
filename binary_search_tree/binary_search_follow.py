class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child=Node(value)
            else:
                self._insert(value, cur_node.left_child)
        else:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
               self._insert(value, cur_node.right_child)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def contains(self, target):
        pass

    def get_max(self):
        pass

def fill_tree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for i in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

print('binary search tree ran')
tree = BinarySearchTree()
tree = fill_tree(tree)

tree.print_tree()