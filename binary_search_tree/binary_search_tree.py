# Implementation using Python's `deque` collection
from collections import deque

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

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else: # value is greater or equal to
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
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
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue
        queue = deque()
        # add root to queue
        queue.append(self)
        # while queue is not empty
        while len(queue) > 0:
            # node = pop head of queue
            node = queue.popleft()
            # DO THE THING! (print)
            print(node.value)
            # add children of node to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create stack
        stack = []
        # add root to stack
        stack.append(self)
        # while stack is not empty
        while len(stack) > 0:
        # node = pop top of stack
            node = stack.pop()
        # DO THE THING! (print)
            print(node.value)
        # add children of node to stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)



if __name__ == '__main__':

    def printing(node):
        print(node)

    bst = BinarySearchTree(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)

    print("For each printing")
    bst.for_each(printing)

    print("In order print")
    bst.in_order_print(bst)

    print("BFT print")
    bst.bft_print(bst)

    print("DFT print")
    bst.dft_print(bst)

    print("Pre-order DFT print")
    bst.pre_order_dft(bst)

    print("Post-order DFT print")
    bst.post_order_dft(bst)
