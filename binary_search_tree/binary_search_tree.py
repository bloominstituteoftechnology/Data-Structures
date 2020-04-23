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
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
                #self.left.right = self
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                #self.right.left = self
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else: # target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        cur = self.right
        if cur == None:
            return self.value
        while cur != None:

            if cur.right == None:
                return cur.value
            cur = cur.right
        return cur.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # apply function to initial value
        self.value = cb(self.value)

        if self.left:
            self.right.for_each(cb)

        if self.right:
            self.right.for_each(cb)

        # #go right, applying cb function  to all values
        # cur = self.right
        # while cur != None:
        #     if cur.right:
        #         cur.value = cb(cur.value)
        #         cur = cur.right
        #     else:
        #         cur.value = cb(cur.value)
        #         cur = None
        # #go left, applying cb function to all values
        # cur = self.left
        # while cur != None:
        #     if cur.left:
        #         cur.value = cb(cur.value)
        #         cur = cur.left
        #     else:
        #         cur.value = cb(cur.value)
        #         cur = None
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
