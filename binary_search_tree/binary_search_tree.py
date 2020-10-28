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

from queue import queue
from stack import stack


class BSTNode:
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
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        if self.value == target:
            return True
        else:
            if self.left.value < target:
                self.right.contains(target)
            else:
                self.left.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            self.right.get_max()

        return self.value

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
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = queue()
        q.enqueue(self)

        while q.size != 0:
            current = q.dequeue()
            print(current.value)

            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):

        s = stack()

        s.push(self)
        while s.size != 0:
            current = s.pop()
            print(current.value)

            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)




    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self:
            print(self.value)
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self:
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            print(self.value)

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
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
