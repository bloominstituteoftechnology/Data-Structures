from queue import Queue
from stack import Stack

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
        # Case 1: Value is less than self.value
        if value < self.value:
            # If there is no left child, then insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # Else: ????
                # Repeat the process on left subtree
                # self.left.insert(value)
            else:
                self.left.insert(value)

        # Case 2: Value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1: self.value == target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value

        found = False

        if self.value >= target:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            found = self.left.contains(target)
        # Case 3: otherwise
        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self is None:
            return None
        # Forget about the left subtree altogether
        # Iterate through the nodes using a loop construct
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Recursive version of get_max() method
    def get_max_(self):
        if self.right is None:
            return self.value
        return self.right.get_max_()

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
        """LEFT--> ROOT--> RIGHT"""
        # if the current node is none we know that we
        # have reached the base case (the end of recursion) and we want to return
        if self is None:
            return
        # check if we can move left
        if self.left is not None:
            self.left.in_order_print(node)

        # visit the node by printing its value
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # Use a queue to form a line for the nodes to "get in"

        queue = Queue()

        # # start by placing the root in the queue
        if node is not None:
            queue.enqueue(node)

        # # need a while loop to iterate
        # what are we checking in the while statement???
        # while length of the queue is greater than 0
            while len(queue) > 0:
                # dequeue item from the front of the queue
                current_node = queue.storage[0]
                print(current_node.value)
                queue.dequeue()
                # print that item
                # place current item's left node in the queue if not None
                if current_node.left is not None:
                    queue.enqueue(current_node.left)
                # place current item's right node in the queue if not None
                if current_node.right is not None:
                    queue.enqueue(current_node.right)
        else:
            return

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):

        # initalize and empty stack and
        stack = Stack()
        # push the root node onto the stack
        if node is not None:
            stack.push(node)
            # need a while loop to manage our iteration
            # if stack is not empty then enter the while loop
            while len(stack) > 0:
                # pop the item(0) off the stack
                current_node = stack.storage[len(stack) - 1]
                print(current_node.value)
                stack.pop()
                # print that items value
                # if there is a right subtree
                # push right item onto the stack
                if current_node.right is not None:
                    stack.push(current_node.right)
                # if there is a left subtree
                # push left item onto the stack
                if current_node.left is not None:
                    stack.push(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        """ROOT --> LEFT --> RIGHT"""

        if self is None:
            return

        print(self.value)

        if self.left is not None:
            self.left.pre_order_dft(node)

        if self.right is not None:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        """LEFT --> RIGHT --> ROOT"""

        if self is None:
            return

        if self.left is not None:
            self.left.post_order_dft(node)

        if self.right is not None:
            self.right.post_order_dft(node)

        print(self.value)
