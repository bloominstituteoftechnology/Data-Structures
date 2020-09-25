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

import sys
sys.path.append('/home/ivan/Desktop/Lambda/CS/Data-Structures/binary_search_tree')
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
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

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return None

        if not self.right:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # initialize function for current node value
        fn(self.value)
        # if left
        if self.left:
            self.left.for_each(fn)
        # if right
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self is None:
            return

        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

        # print(self.value)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        new_queue = Queue()
        new_queue.enqueue(self)

        while new_queue:
            current_node = new_queue.dequeue()
            print(current_node.value)

            if current_node.left:
                new_queue.enqueue(current_node.left)

            elif current_node.right:
                new_queue.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        new_stack = Stack()
        new_stack.push(self)

        while new_stack:
            current_node = new_stack.pop()
            print(current_node.value)

            if current_node.left:
                new_stack.push(current_node.left)

            elif current_node.right:
                new_stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)

        if self.left:
            self.left.pre_order_dft()

        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()

        if self.right:
            self.right.post_order_dft()

        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
