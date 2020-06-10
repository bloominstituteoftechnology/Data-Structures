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
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # value == target
        if self.value == target:
            return True
        # value != target
        else:
            # is the target lower than the value?
            if target < self.value:
                # is there any child node?
                if not self.left:
                    return False
                # is the left child node our target?
                if self.left.value == target:
                    return True
                else:
                    self.left.contains(target)
            else: # target >= self.value
                # is there any child node?
                if not self.right:
                    return False
                # is the right child node our target?
                if self.right.value == target:
                    return True
                else:
                    self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # self.left.value will always ne smaller than the root
        # so we have to check only the self.right path
        if not self.right:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function `fn`
        fn(self.value)
        # go to the left node if any
        if self.left:
            self.left.for_each(fn)
        # go to the right node if any
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
