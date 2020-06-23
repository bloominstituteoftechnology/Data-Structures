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
        # value is less than the root go left
        if value < self.value:
            # if there is no value on the left side
            if not self.left:
                # value becomes the root of the new subtree
                self.left = BSTNode(value)
            else:
                # insert the the value
                self.left.insert(value)

        else:
            # go right
            # if there is no value on the right side
            if not self.right:
                # value becomes the root of the new subtree
                self.right = BSTNode(value)
            else:
                # insert the the value
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if root equals target
        if self.value == target:
            # return True
            return True
    # Check on the left side
        if self.left:
            # if left side contains target
            if self.left.contains(target):
                # return True
                return True
    # Check on the right side
        if self.right:
            # if right side conatins target
            if self.right.contains(target):
                # return True
                return True
    # otherwise, return False
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check if there is no node on the right
        if not self.right:
            # return self.value
            return self.value
        # keep moving to the right for as long as you can
        # then return the node at the end of it all
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
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
