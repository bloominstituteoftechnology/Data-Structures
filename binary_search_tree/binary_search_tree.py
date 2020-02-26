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
    def insert(self, num):
        # base case:
        # if there is no node at root:
        if (self.value == None):
            # insert this node at root
            self = BinarySearchTree(num)
            return

        else:
            # compare value to the root
            if num < self.value:
            # if value < root:
                # look left,
                if self.left is not None:
                    #if node: repeat steps
                    return self.left.insert(num)
                else:
                    # else: no node, make new one w this value 
                    self.left = BinarySearchTree(num)
            # if value >= root:
            if num >= self.value:
                # look right
                if self.right is not None:
                    #if node: repeat steps
                    return self.right.insert(num)
                    # else, no node, make new one w this value
                else:
                    self.right = BinarySearchTree(num)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # if value < root, go left
        elif self.left and target < self.value:
            return self.left.contains(target)
        elif self.right and target >= self.value:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
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

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
