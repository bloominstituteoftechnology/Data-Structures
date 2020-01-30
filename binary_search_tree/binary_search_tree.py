# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


# Binary Search Tree - discards duplicate values
class BinarySearchTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    # Insert the given value into the tree
    def insert(self, value):
        newNode = None
        if value < self.value:
            if self.left:
                newNode = self.left.insert(value)
            else:
                newNode = BinarySearchTree(value, self)
                self.left = newNode
        elif value > self.value:
            if self.right:
                newNode = self.right.insert(value)
            else:
                newNode = BinarySearchTree(value, self)
                self.right = newNode
        return newNode

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.left is None and self.right is None:
            return False
        else:
            if target < self.value:
                return self.left.contains(target)
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        theMax = self.value
        if self.right:
            theMax = self.right.get_max()
        return theMax

    # Return the minimum value found in the tree
    def get_min(self):
        theMin = self.value
        if self.left:
            theMin = self.left.get_min()
        return theMin

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

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
