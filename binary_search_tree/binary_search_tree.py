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
        # compare input value with value of node
        # value < node's value
        if value < self.value:
            # go left
            # if there is no left child, park the value in bst node
            if self.left is None:
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left's child's insert method
                return self.left.insert(value)
        # otherwise value >= nodes value
        else:
            # go right
            # if there is no right child, wrap in bst node and park
            if self.right is None:
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                return self.right.insert(value)
            # call the left's child's insert method

        # Return True if the tree contains the value
        # False if it does not
    def contains(self, target):
        # base case
        # check root node against target
        # if target == root
        if target == self.value:
            return True
        # return true
        # if the target >= root
        # go right
        if target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
                # recursion
        # otherwise target < root
        # go left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
                # recursion

    # Return the maximum value found in the tree
    def get_max(self):
        # if right is true
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, func):
        func(self.value)
        if self.right:
            self.right.for_each(func)
        if self.left:
            self.left.for_each(func)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# # bst.in_order_print()
# print("post order")
# bst.post_order_dft()
