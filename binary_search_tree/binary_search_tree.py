import sys
sys.path.append('queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare to root node
        # If lesser go to left child
        if (value < self.value):
            if (self.left is None):
                # insert
                self.left = BinarySearchTree(value)
            else:
                # move left
                self.left.insert(value)
        # If greater or equal to, go right
        elif (value >= self.value):
            if (self.right is None):
                # insert
                self.right = BinarySearchTree(value)
            else:
                # move right and go through insert function
                self.right.insert(value)     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If root is target, return
        if (target == self.value):
            return True
        elif (target < self.value):
            if (self.left is None):
                return False
            else:
                # move left
                # repeat
                return self.left.contains(target)
        elif (target >= self.value):
            if (self.right is None):
                return False
            else:
                # move right
                # repeat
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Keep going right until no child is found.
        if (self.right is None):
            maximum = self.value
            return maximum
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if (self.left is not None and self.right is not None):
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif (self.left is not None):
            self.left.for_each(cb)
        elif (self.right is not None):
            self.right.for_each(cb)
        else:
            return
        

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

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
