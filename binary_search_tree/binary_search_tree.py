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

        # let's set some conditionals:
        if type(value) is not int:
            raise ValueError("Not an Int")
        if self.value == None:
            self.value = value
            return
        elif value < self.value:       # we are referring to the value passed in through insert
            if not self.left:                     # if not there, then we add the value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value >= self.value:        # if it is greater, we go to the right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if type(target) is not int:
            raise ValueError("not an int")
        if self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # recursion?
        # if no right child, return this value, otherwise go right
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
    # if you are trying to find something/answer using recursion, you have to return it

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # traverse the tree. Go through each node and execute the function

    def for_each(self, cb):

        print(self.value)
        cb(self.value)
        if self.left:
            print('left')
            self.left.for_each(cb)
        if self.right:
            print('right')
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
