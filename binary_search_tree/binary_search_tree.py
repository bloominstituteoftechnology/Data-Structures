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
        curr_node = self

        while True:
            if value >= curr_node.value:
                if curr_node.right is None:
                    curr_node.right = BSTNode(value)
                    return curr_node.right
                else:
                    curr_node = curr_node.right
            elif value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BSTNode(value)
                    return curr_node.left
                else:
                    curr_node = curr_node.left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        curr_node = self

        while True:
            if curr_node.value == target:
                return True
            if target > curr_node.value:
                if curr_node.right is None:
                    return False
                else:
                    curr_node = self.right
            elif target < curr_node.value:
                if curr_node.left is None:
                    return False
                else:
                    curr_node = self.left

    # Return the maximum value found in the tree
    def get_max(self):

        max_value = 0
        curr_node = self

        while True:
            if curr_node.value > max_value:
                max_value = curr_node.value
            elif curr_node.right is None:
                return max_value
            else:
                curr_node = curr_node.right

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        print("for_each - self:", self, self.left, self.right)
        if self is None:
            return
        fn(self.value)
        self.for_each(fn(self.right))
        self.for_each(fn(self.left))

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
