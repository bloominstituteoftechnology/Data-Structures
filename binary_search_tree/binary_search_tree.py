import sys
sys.path.append('../stack')
from queue import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # If there is no "left" value
            if self.left == None:
                self.left = BSTNode(value)
            # Start over at the "left" position
            else:
                self.left.insert(value)
        else:
            # If there is no "right" value
            if self.right == None:
                self.right = BSTNode(value)
            # Start over at the "right" position
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            # If there's nothing at all to the left, this value
            # does not exist in the tree
            if self.left == None:
                return False
            # Begin a recursive cycle to check the "left" nodes
            else:
                return self.left.contains(target)
        else:
            # If there's nothing at all to the right, this value
            # does not exist in the tree
            if self.right == None:
                return False
            # Begin a recursive cycle to check the "right" nodes
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # There's no node to the right! Nothing is larger!
        if self.right == None:
            return self.value
        # There's a node to the right! Let's keep looking!
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call the function on the current value
        fn(self.value)

        if self.left:
            # Make the left node the current value
            self.left.for_each(fn)
        if self.right:
            # Make the right node the current value
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.put(node)

        while storage.qsize() > 0:
            node = storage.get()
            print(node.value)

            if node.left:
                storage.put(node.left)
            if node.right:
                storage.put(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)

        while storage.size > 0:
            node = storage.pop()
            print(node.value)

            if node.left:
                storage.push(node.left)
            if node.right:
                storage.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
