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
        if self.value is None:
            return None
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value != None:
            fn(self.value)
            if self.left is not None and self.right is not None:
                self.left.for_each(fn)
                self.right.for_each(fn)
            elif self.right is not None:
                # fn(x = self.right.value)
                self.right.for_each(fn)
            elif self.left is not None:
                # fn(x = self.left.value)
                self.left.for_each(fn)
            elif self.left is None and self.right is None:
                return None
            # return fn(x = self.value)
        else:
            return None

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
            self.left.in_order_print(node)

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # if the current node is None
        if self is None:
            return
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        queue = Queue()
        # start by placing the root in the queue
        queue.enqueue(node)

        # while length of queue is greater than 0
        while queue.__len__() > 0:
            # dequeue item from front of queue
            n = queue.dequeue()
            # print that item
            print(n.value)

            # place current item's left node in queue if not None
            if n.left is not None:
                queue.enqueue(n.left)
            # place current item's right node in queue if not None
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
        # if the current node is None
        if self is None:
            return
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        queue = Queue()
        # start by placing the root in the queue
        queue.enqueue(self.value)
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while queue.__len__() > 0:
            # place current item's right node in queue if not None
            if self.right is not None:
              self.right.bft_print(node)

            # dequeue item from front of queue
            value_to_print = queue.dequeue()
            # print that item
            print(value_to_print)

            # place current item's left node in queue if not None
            if self.left is not None:
              self.left.bft_print(node)
