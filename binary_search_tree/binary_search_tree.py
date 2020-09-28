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
sys.path.append('../queue')
from dll_queue import dll_queue
sys.path.append('../stack')
from dll_stack import dll_Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if root is not empty and value is greater than root, place value to right of root
        if (value >= self.value) and (self.right != None):
            self.right.insert(value)
        # if root is empty and value is greater than root, create a node and place value to right of root
        if (value >= self.value) and (self.right == None):
            new_node = BSTNode(value)
            self.right = new_node
        # if root is not empty and value is lesser than root, place value to right of root
        if (value < self.value) and (self.left != None):
            self.left.insert(value)
        # if root is empty and value is lesser than root, create a node and place value to left of root
        if (value < self.value) and (self.left == None):
            new_node = BSTNode(value)
            self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if (target>self.value):
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        if (target<self.value):
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        curr_node = self
        # print(curr_node.value)
        while curr_node.right:
            curr_node=curr_node.right
        return curr_node.value


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
    def in_order_print(self):
        # goto the left and bottomost node and print that value to its left
        # now print value of node iteself
        # then goto right and print that value
        # recurse until all values are printed. 
        if self.left:
            self.left.in_order_print()
        print (self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for nodes
        # add first node to the queue
        # while queue is not empty
            # remove the first node from the queue
            # print the remove node
            # add children into the queue
        queue = dll_queue()
        queue.enqueue(self)
        while len(queue)>0:
            curr_node = queue.dequeue()
            print (f'Value of current node is {curr_node.value}')
            if curr_node.left: 
                queue.enqueue(curr_node.left)
            if curr_node.right: 
                queue.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # Create a stack for the nodes
        # add the first node to stack 
        # add the the children to the stack. keep in mind to add these in same order. 
        stack = dll_Stack()
        stack.push(self)

        while len(stack)>0:
            curr_node = stack.pop()
            print(f'Value of current node is {curr_node.value}')
            if curr_node.left: 
                stack.push(curr_node.left)
            if curr_node.right: 
                stack.push(curr_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

#bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
