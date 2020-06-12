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
            # checks for value on left
            if not self.left:
                self.left = BSTNode(value)
            # Inserts on left
            else:
                self.left.insert(value)
        else:
            # checks for right node and sets it
            if not self.right:
                self.right = BSTNode(value)
            else:
                # inserts on the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value === target:
            return True
        elif target < self.value:
            if self.left:
                # checks the contents
                return self.left.contains(target)
        else:
            if self.right:
                # checks the contents
                return self.right.contains(target)
        #is not contained
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        # will rewrite current node right
        while current_node.right:
            current_node = current_node.right
        return current_node.value

        # if self.right is None:
        #     return self.value
        # else:
        #     return self.right.get_max()

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
