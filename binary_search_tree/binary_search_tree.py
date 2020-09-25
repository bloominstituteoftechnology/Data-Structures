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
from queue import Queue
from stack import Stack


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
            # ELSE Repeat the process on left subtree
            else:
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1: If self.value is equal to the target
        if self.value == target:
            return True

        # Case 2: if target is less than self.value
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
        if self.right is not None:
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
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(self.left)

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line"
        # for the nodes to "get in"

        # start by placing the root in the queue

        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item

        # place current item's left node in queue if not None
        # place current item's right node in queue if not None

        q = Queue()
        q.enqueue(self)
        while len(q) > 0:

            dequeued = q.dequeue()
            print(dequeued.value)

            if dequeued.left is not None:
                q.enqueue(dequeued.left)
            if dequeued.right is not None:
                q.enqueue(dequeued.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):

        # initialize an empty stack
        # push the root node onto the stack

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        # pop top item off the stack
        # print that item's value

        # if there is a right subtree
        # push right item onto the stack

        # if there is a left subtree
        # push left item onto the stack
        s = Stack()
        s.push(self)

        while len(s) > 0:

            popped = s.pop()
            print(popped.value)

            if popped.right:
                s.push(popped.right)

            if popped.left:
                s.push(popped.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        print(self.value)

        if self.left:
            self.left.pre_order_dft(self)
        if self.right:
            self.right.pre_order_dft(self)
        # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self)
        if self.right:
            self.right.post_order_dft(self)

        print(self.value)
