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
import sys
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # insert
        # left case
        # check if our value is less than root value
        if value < self.value:
            # move to the left and check if it is None
            if not self.left:
                # insert node here set the self.left to the new node
               self.left = BSTNode(value)
            # otherwise
            else:
                # do an insert on the root's left node recursive call to the left node using self.left
                return self.left.insert(value)
        # right case
        # otherwise
        else:
            # move to the right and check if it is None
            if self.right is None:
                # insert node here set the self.right to the new node
               self.right = BSTNode(value)
            # otherwise
            else:
                # do an insert on the root's right node recursive call to insert using self.right
                return self.right.insert(value)
      

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
         # contains
        # check the value root node (self.value) against the target
        # if the root node value and target are the same
        if self.value == target:
            # return True
            return True
        
        # left case
        # check if our target is less than the root val (self.value)
        elif target < self.value:
            # check if there is no child to the left (self.left) is None
            if not self.left :
                # return False
                return False
            # otherwise
            else:
                # call contains on the left child (self.left)
                return self.left.contains(target)
        
        # right case
        # otherwise
        else:
            # check if there is no child to the right (self.right) is None
            if not self.right:
                # return False
                return False
            # otherwise
            else:
                # call contains on the right child (self.right)
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # move to the right and check if it is not None return None
        # if tree is empty return None
        if not self:
            # return None
            return None
            # iterative approach
            # while there is right child
        while self.right:
            # move to the child
            self = self.right
            # return a self.value once there is no right child
            # when return is inside the loop then it stops the loop to the first node 
            # and the operation stops.
            # when return is outside of the loop then loop continue the operation further down to the right side of the node
            # until it reaches the end.
        return self.value
       

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # callback the function on the self.value
        # cb function is a function passed into another function as an argument
        # which is then invoked inside the outer function to complete some kind of action
        fn(self.value)
        # check if it is true and use for_each to make recursive call in the self.left side 
        if self.left:
            self.left.for_each(fn)
        # check if it is true and use for_each to make a recursive call in the self.right side
        if self.right is True:
            return self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # base case
        # if our node does not exist
        if not self:
             # return None
             return None
      
        # left case
        # if left exists
        if self.left:
             # call in order print on self.left
             self.left.in_order_print(self.left)
        
        # print the node value
        print(self.value)

        # right case
        # if right exists
        if self.right:
             # call in order print on self.right
             self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # instantiate a queue
        q = Queue()
        # enqueue our starting node (self)
        queue.enqueue(self)
        # while the queue has data
        while q.len() > 0:
            # dequeue the current node
            current_node = queue.dequeue()
            # print the nodes value
            print(current_node.value)
            # check if a left child exists
            if current_node.left:
                # enqueue left child
                queue.enqueue(current_node.left)
            # check if right child exists
            if current_node.right:
                # enqueue right child
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # instantiate a stack
        s = Stack()
        # push our starting node (self)
        s.push(node)
        # while the stack has data
        while stack.len() > 0:
            # pop the current node
            current_node = s.pop()
            # print the nodes value
            print(current_node.value)
            # check if a left child exists
            if current_node.left:
                # push left child
                s.push(current_node.left)
            # check if right child exists
            if current_node.right:
                # push right child
                s.push(current_node.right)
  
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
