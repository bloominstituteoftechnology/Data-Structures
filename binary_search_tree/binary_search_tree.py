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
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.left and target < self.value:
            return self.left.contains(target)
        if self.right:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if self.value == None:
        #     return
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.value

        if node.right:
            node.right.dft_print()
        if node.left:
            node.left.dft.print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()

            # check if this node has children 
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        return self.value

        if self.right:
            self.right.dft_print()
        if self.left:
            self.left.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_print(self):

        # First return/print the value of the node.
        return self.value

        # Check if there is a left lead, if so call call pre_order recursively on the leaf.
        if self.left:
            self.left.pre_order_print()

        # Check if there is a right lead, if so call call pre_order recursively on the leaf.
        if self.right:
            self.right.pre_order_print()

    # Print Post-order recursive DFT
    def post_order_print(self):
        # First check if there is a left leaf, if so, recursively call post_order_print on left leaf
        if self.left:
            self.left.post_order_print()
        # First check if there is a right leaf, if so, recursively call post_order_print on right leaf
        if self.right:
            self.right.post_order_print()
        # Return / print the value of self
        return self.value

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_print()
print("in order")
bst.in_order_print(bst)
print("post order")
bst.post_order_print() 