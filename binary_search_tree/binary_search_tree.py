import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return

        # BST was empty
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # insert into RIGHT subtree 
        elif value >= self.value:
            # TBC 
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # insert into LEFT subtree:
        else: 
            # TBC 
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # 1. Base cases:
        # target found OR we hit None

        # 2. Recursive case 
        # go down left or right subtree
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # RIGHT as far as you can go 
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # calling function on current node 
        cb(self.value)

        # 1. Base case:
        # Left is None or Right is None 
        if self.left is None and self.right:
            # do nothing 

        # 2. Recurisvie case:
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        
        # 1. Base case:
        # else both are None, stop recursion

    def iter_for_each(self, cb):
        if self is None:
            # print msg, BST is empty
            return

        cb(self.value)
        while 
            # go left, go right

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
