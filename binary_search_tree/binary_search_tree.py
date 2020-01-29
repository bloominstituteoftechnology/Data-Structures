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
        # compare root node  --  maybe not true
        while self.value != value:
        # variable for value

        # current node too
            current_node = None
        # if lesser go to left child
            if self.value < value:
                self.value = self.left


        # if greater go to right child
            if self.value >= value:
                self.value = self.right
        # if not child, on that side, insert else try again starting from the child on appropriate

            self.value == value

    # Return True if the tree contains the value
    # False if it does not
    # Find
    # look at root, if root is it return
    # if value is less than node, go left and repeat
    # if no left child, return none
    # if value is >= node, go right and repeat. if not right child return none
    # and then something... maybe 3 statements in while loop
    # variables? at least 2
    def contains(self, target):
        # easiest is it the root?
        if self.value == target:
            return True
        while self.value is not target:
            if self.value >= target:
                self.value = self.left
            if self.value < target:
                self.value = self.right
            if self.right == None and self.left == None:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        # go right until no more
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
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

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

    def delete_node(self, node):
        pass