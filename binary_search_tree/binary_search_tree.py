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

import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

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
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # 1. Base case - no more nodes in our subtree
        # 2. Recursive case
        fn(self.value)
        if self.left: # same as is not None
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

     # STRETCH
    def delete(self, value):
        # if self.contains(value):
        # different cases
        # if node at bottom level
            # updated parent lef/right = None
        # if node is an only child
            # parent.left/right = node.left/right
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
            # inOrder
            if self.left:
                # go left with recursion
                self.left.in_order_print()
            print(self)
            if self.right:
                # go right with recursion
                self.right.in_order_print()
            print(self)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def in_order_dft(self):
        self.in_order_print()


    def bft_print(self):
        # create a stack
        queue = []
        # push some initial value(s) onto the stack
        queue.append(self)
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack
        stack = []
        # push some initial value(s) onto the stack
        stack.append(self)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

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
