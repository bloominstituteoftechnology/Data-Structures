"""
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import LifoQueue, SimpleQueue

class BinarySearchTree:
    """
    Binary search trees are a data structure that enforce an ordering over
    the data they store. That ordering in turn makes it a lot more efficient
    at searching for a particular piece of data in the tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Insert the given value into the tree.
        """
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        """
        Return True if the tree contains the value, false if it does not.
        """
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        """
        Return the maximum value found in the tree.
        """
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, fn):
        """
        Call the function `fn` on the value of each node.
        """
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    def in_order_print(self, node):
        """
        Print all the values in order from low to high.
        Hint: Use a recursive, depth first traversal.
        """
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    def bft_print(self, node=None):
        """
        Print the value of every node, starting with the given node, in an
        iterative breadth first traversal.
        """
        if node is None:
            node = self
        
        to_print = SimpleQueue()
        to_print.put(node)
        while to_print.qsize() != 0:
            node = to_print.get()
            print(node.value)
            if node.left is not None:
                to_print.put(node.left)
            if node.right is not None:
                to_print.put(node.right)

    def dft_print(self, node=None):
        """
        Print the value of every node, starting with the given node,
        in an iterative depth first traversal.
        """
        if node is None:
            node = self
            
        retrace = LifoQueue()
        print(node.value)
        retrace.put(node)
        while node.left is not None:
            node = node.left
            print(node.value)
        while retrace.qsize() != 0:
            node = retrace.get().right
            if node is not None:
                print(node.value)
                while node.left is not None:
                    retrace.put(node)
                    node = node.left
                    print(node.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        """
        Print Pre-order recursive DFT.
        """
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        """
         Print Post-order recursive DFT.
        """
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)
