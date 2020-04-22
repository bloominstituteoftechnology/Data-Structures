from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new nodes value is less than out current nodes value
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value) 
        else: ## for when the value is equal to node value
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            # if there is no left child already here
                # place a new bst with the value passed in to the left
            # otherwise
                # repeat the process recursively on the left
        
        # else if the value is greater than or equal to the current nodes value
            # if there is no right child already here
                # place a new bst with the value passed in to the right
            # otherwise
                # repeat the process recursively on the right

        # Return True if the tree contains the value
        # False if it does not
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
         # base case. if value matches current target
            # return True
        if self.value == target:
            return True
        if target < self.value:
            if not self.left: ## check if the left contains the value then repeat for the right 
                return False
            else:
                return self.left.contains(target)
        else: 
            if not self.right:
                return False
            else: 
                return self.right.contains(target)
        # if target less than value 
            # check left child recursively
            # if no left child
                # return false
            # otherwise
                # call contains on the left
        # otherwise
            # check right child recursively
            # if no right child
                # return false
            # otherwise
                # call contains on the right
        

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
         # do the call back using self.value as the parameter
        cb(self.value)
        # if left exists
            # call foreach on left
        if self.left:
            self.left.for_each(cb)
        

        # if right exists
            # call foreach on right
        if self.right:
            self.right.for_each(cb)
        

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
