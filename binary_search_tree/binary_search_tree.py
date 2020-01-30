from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree


def insert(self, value):
        # pass
        # if input is less than parent value, move to left
        if value < self.value:
            # Create a new binary search tree inputting incoming as value
            if self.left == None:
                self.left = BinarySearchTree(value)
            # if there's already an element, slide down and make BST with recursion
            else:
                self.left.insert(value)
        # if input is more, move to right pointer
        else:
            # Create a new BST inputting incoming value as value
            if self.right == None:
                self.right = BinarySearchTree(value)
            # if there's already an element, slide down and make BST with recursion
            else:
                self.right.insert(value)s

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        if self.value == target:
            return True
        # if target value is > parent, traverse right
        elif target > self.value:
            # if self.right = None return False
            if self.right == None:
                return False
            # else, call contains recursively
            else:
                return self.right.contains(target)
        # if not, traverse left
        elif target < self.value:
            # if current value = None return False
            if self.left == None:
                return False
            # else call contains recursively
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # pass
        cb(self.value)
        # recursive go left
        if self.left != None:
            self.left.for_each(cb)
        # recursive go right
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
            # if there is a left, run recursive function on left
        # print self
        # if there is a right, run recursive function on right
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

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
