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
        # compare the value to the rott's value to determing which direction we're going in
        # if the value < root's value
        if value < self.value:
            # go left
            # we have to check if there is another node on the left side
            if self.left:
                # compare again
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # else the value >= root's value
        else:
            # go right
            # we have to check if there is another node on the right side
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        return self.right.get_max() if self.right else self.value
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        
    def iter_depth_first_for_each(self, fn):
        # with depth first traversal, there;s a certain to when we visit nodes
        # what's the order?
        # init a stack to keep track of the order of nodes visited
        stack = []
        # add the first node to our stack
        stack.append(self)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack
            # add the right child first and left child second to ensure that left is popped off the stack first
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
                # call the fn function on self.value
            fn(self.value)

    def iter_breadth_first_for_each(self, fn):
        # breadth first follows FIFO ordering for its nodes
        # init a deque
        queue = deque()
        # add the first node to our queue
        queue.append(self)

        while len(queue) > 0:
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current_node = stack.pop()

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
