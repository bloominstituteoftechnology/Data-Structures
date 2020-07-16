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
        # CASE 1: If value is less than self.value (left)
        if value < self.value:
            # If there is no left child, create node with the value there
            if self.left is None:
                self.left = BSTNode(value)
            # Else
            else:
                # Recursion: Repeat the process on the left subtree by calling insert again
                self.left.insert(value)

        # CASE 2: If value is greater than or equal than self.value (right)
        if value >= self.value:
            # if there is no right child, insert value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat process on right subtree
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
        # Case 3: Otherwise
        else:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # No need to check left subtree
        # Will need to iterate through
        if self.right is not None:
            # if greater node exists, repeat
            return self.right.get_max()
        if self.right is None:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if node exists to left
        if self.left is not None:
            self.left.for_each(fn)
        # if node exists to right
        if self.right is not None:
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
            self.left.in_order_print(node.left)

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node.right)

        
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        q = Queue()

        # start by placing the root in the queue
        q.enqueue(self)

        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while q.size > 0:
            # dequeue item from front of queue
            dequeuing_node = q.dequeue()
            # print that item
            print(dequeuing_node.value)

            # place current item's left node in queue if not None
            if dequeuing_node.left is not None:
                q.enqueue(dequeuing_node.left)
            # place current item's right node in queue if not None
            if dequeuing_node.right is not None:
                q.enqueue(dequeuing_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        stack.push(self)

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        while stack.size > 0:
            # pop top item off the stack
            popping_node = stack.pop()
            # print that item's value
            print(popping_node.value)

            # if there is a right subtree
            if popping_node.right is not None:
                # push right item onto the stack
                stack.push(popping_node.right)
                
            # if there is a left subtree
            if popping_node.left is not None:
                # push left item onto the stack
                stack.push(popping_node.left)