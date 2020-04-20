'''
from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')
'''


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        while self:
            if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                    return
                else:
                    self = self.left
            else:
                if not self.right:
                    self.right = BinarySearchTree(value)
                    return
                else:
                    self = self.right

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        while self:
            if target is self.value:
                return True
            elif target < self.value:
                if not self.left:
                    return False
                else:
                    self = self.left
            else:
                if not self.right:
                    return False
                else:
                    self = self.right

    # Return the maximum value found in the tree

    def get_max(self):
        # Initially set the max value to be self.
        max = self.value
        while self.right:
            if self.right.value > max:
                max = self.right.value
            self = self.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left:
            self.left.for_each(cb)
        elif self.right:
            self.right.for_each(cb)
        else:
            pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
