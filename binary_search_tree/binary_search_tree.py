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
# import os
# import sys
# sys.path.append(f'{os.getcwd()}/singly_linked_list')
# from singly_linked_list import LinkedList, Node
from queue import Queue
# from stack import Stack

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
        # Case 1: self.value is equal to target
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
        # Skip left side of BST when finding max value
        if self.right is None:
            return self.value # self.value == current node
        else:
            return self.right.get_max()

        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # run fn on self.value (current node)
        if self.left: # check if left side of tree exists
            self.left.for_each(fn) # run fn on each value on left
        if self.right: # check if right side of tree exists
            self.right.for_each(fn) # run fn on each value on right

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        # inorder
        if self is None:
            return
        # recurse  left
        if self is not None:
            if self.left:
                self.left.in_order_print(self)
        # visit logic
            print(self.value)
        # recurse right
            if self.right:
                self.right.in_order_print(self)
                

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):        
        # use a queue to form a 'line'
        # for the nodes to 'get in'
        queue = Queue()        
        # start by placing the root in the queue
        queue = enqueue(node)
        # need a while loop to iterate
        # while length of queue is greater than 0
        while queue.size > 0:
        # what are we checcking in the while statement?
            # dequeue item from front of queue
            # print that item     
            current_node = queue.dequeue()
            print(current_node.value)
            # place current items left node in queue if not None
            if current_node.left:
                queue.enqueue(current_node.left)
            # place current items right node in queue if not None
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal    
    def dft_print(self, node):
        
        # initialize an empty stack
        stack = []
        # push the root node onto the stack
        stack.append(node)
        # need a while loop to manage our iteration
        
        # if stack is not empty enter the while loop
        while len(stack) != 0:
            # pop top item off the stack
            current_node = stack.pop()
            # print that item's value
            print(current_node.value)
            # if there is a left subtree
            if current_node.left:
                # push left item onto stack
                stack.append()
            # if there is a right subtree
            if current_node.right:
                # push right item onto stack
                stack.append()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(current)
        while stack.__len__() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.right:
                stack.push(popped.right)
            if popped.left:
                stack.push(popped.left)

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass

if __name__ == '__main__':
    pass