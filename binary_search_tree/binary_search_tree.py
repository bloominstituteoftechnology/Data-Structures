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
        if self.value == target: #is equal
            return True
        elif target < self.value: # is smaller
            if self.left: # call and return contains on existing left node
                return self.left.contains(target)
            else:
                return False # if no left node
        else: # is greater
            if self.right: # call and return contains on existing right node
                return self.right.contains(target)
            else:
                return False # if no right node

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.contains(target)

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):     # so left > root > right
        if node.left:
            self.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative **breadth** first traversal
    # use queue, 
    # can implement with python's 'deque' collection
    # https://docs.python.org/2/library/collections.html#collections.deque

    def bft_print(self, node):
        queue = deque()
        queue.append(self) #create and add queue root
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
    # in an iterative **depth** first traversal
    # use stack instead of queue
    def dft_print(self, node):
        stack = []
        stack.append(self) #create and add stack root
        # while stack is not empty
        while len(stack) > 0:
            # node = pop head of stack
            node = stack.pop()
            # DO THE THING! (print)
            print(node.value)
            # add children of node to stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required
    # same function calls just printing in different order
    
    ### still getting error on line 100 in test (?!)

    # Print **Pre**-order recursive DFT
    # root > left > right 
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.left.in_order_print(node.left)
        if node.right:
            self.right.in_order_print(node.right)

    # Print **Post**-order recursive DFT
    # left > right > root
    def post_order_dft(self, node):
        if node.left:
            self.left.in_order_print(node.left)
        if node.right:
            self.right.in_order_print(node.right)
        print(node.value)