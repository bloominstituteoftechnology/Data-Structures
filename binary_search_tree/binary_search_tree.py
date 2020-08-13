# python3 binary_search_tree/test_binary_search_tree.py -v
from queue.queue import Queue
from stack.stack import Stack

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


    def insert(self, value):
        if value < self.value:
            if self.left is None:
               self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
               self.right = BSTNode(value)
            else:
                self.right.insert(value)


    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    def get_max(self):
        if self.value is None:
            return None
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()


    def for_each(self, fn):
        if self.value != None:
            fn(self.value)
            if self.left is not None and self.right is not None:
                self.left.for_each(fn)
                self.right.for_each(fn)
            elif self.right is not None:
                self.right.for_each(fn)
            elif self.left is not None:
                self.left.for_each(fn)
            elif self.left is None and self.right is None:
                return None
        else:
            return None

# Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print(node)
        # visit the node by printing its value
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(node)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # if the current node is None
        if self is None:
            return
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            n = queue.dequeue()
            print(n.value)

            if n.left is not None:
                queue.enqueue(n.left)
            if n.right is not None:
                queue.enqueue(n.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # if the current node is None
        if self is None:
            return
        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        stack.push(self.value)
        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        while stack.__len__() > 0:
            # pop top item off the stack
            value_to_print = stack.pop()
            # print that item's value
            print(value_to_print)
            # if there is a right subtree
            if self.right is not None:
                # push right item onto the stack
                self.right.dft_print(node)
                
            # if there is a left subtree
            if self.left is not None:
                # push left item onto the stack
                self.left.dft_print(node)

    def bft_print_high_to_low(self, node):
        if self is None:
            return
        queue = Queue()
        queue.enqueue(self.value)
        while queue.__len__() > 0:
            if self.right is not None:
              self.right.bft_print(node)

            value_to_print = queue.dequeue()
            print(value_to_print)

            if self.left is not None:
              self.left.bft_print(node)

# Stretch Goals -------------------------
# Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if self is None:
            return
        queue = Queue()
        queue.enqueue(self.value)
        while queue.__len__() > 0:

            value_to_print = queue.dequeue()
            print(value_to_print)

            if self.left is not None:
              self.left.pre_order_dft(node)

            if self.right is not None:
              self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self is None:
            return
        stack = Stack()
        stack.push(self.value)
        while stack.__len__() > 0:

            if self.left is not None:
                self.left.post_order_dft(node)

            if self.right is not None:
                self.right.post_order_dft(node)

            value_to_print = stack.pop()
            print(value_to_print)
