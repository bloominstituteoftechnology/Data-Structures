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
        if value >= self.value:
            if self.right == None: # value is greater than or equal to the node currently referred to as self and there is not another node that fits that description.
                self.right = BSTNode(value)
            else:
                self.right.insert(value) # rerun this method with the correct child node
        else:
            if self.left == None: # value is less than the node currently referred to as self and there is not another node that fits that description.
                self.left = BSTNode(value)
            else:
                self.left.insert(value) # rerun this method with the correct child node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        # start at root and run this method on each of the node's children (if any)
        if self.left != None:
            self.left.for_each(fn)
        if self.right != None:
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
