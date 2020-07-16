"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
​
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import random
from queue_stuff.queue import Queue
from stack.stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
               self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
               self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # One liner because I can.
        return self.value if self.right is None else self.right.get_max()

        # Non-one liner
        # if self.right is not None:
        #     return max(self.value, self.right.get_max())
        # else:
        #     return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        for i in [self.left, self.right]:
            if i is not None:
                i.for_each(fn)
        return fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return
        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print()

        # visit the node by printing its value
        print(self.value)
        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # You should import the queue_stuff class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" for the nodes to "get in"
        q = Queue()
        # start by placing the root in the queue_stuff
        q.enqueue(node)
        iteration = 0
        while q.size > 0:
            current_node = q.dequeue()
            print(current_node.value)
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)


        # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)

        x_arr = []
        while s.size > 0:
            current_node = s.pop()
            print(current_node.value)
            x_arr.append(current_node.value)
            if current_node.left:
                s.push(current_node.left)
            if current_node.right:
                s.push(current_node.right)
        # print("XARR", x_arr)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        #Pre order prints when an element is first encountered.
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        #Post order prints when an element has no more children to process.
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)

        print(node.value)
