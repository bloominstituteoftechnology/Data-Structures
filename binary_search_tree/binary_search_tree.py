"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if the value is less than the node's value
        if value < self.value:
            # if left is None
            if not self.left:
                # create new left node
                self.left = BSTNode(value)
            else:
                # insert the value on the left
                self.left.insert(value)
        else: # the value is greater than or equal to nodes value
            # if right node is None
            if not self.right:
                # create the new right node
                self.right = BSTNode(value)
            else:
                # insert the value on the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False

            return self.left.contains(target)
        else:
            if not self.right:
                return False

            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check right side because it's at least equal to or greater than current root
        if self.right:
            # if there is a right node, repeat function
            return self.right.get_max()
        else:
            # if there isn't a right node, maximum value has been found
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if there is a left node
        if self.left:
            # call for_each
            self.left.for_each(fn)
        # if there is a right node
        if self.right:
            # call for_each
            self.right.for_each(fn)

    # Part 2 -----------------------

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

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
