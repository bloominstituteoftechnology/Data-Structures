import sys
from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
​
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
        # check if the value is less than the current node's value 
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here 
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value 
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child 
            # we can park the new node here 
            else:
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # value is not optional, would need to check for nil otherwise.
        # 5.for_each(fn)
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)  # work through left side of nodes and append values.
        if self.right is not None:  # check right side as we work through the stack.
            self.right.for_each(fn)  # append values to test array if value is not none.
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
    # Call the function `fn` on the value of each node
    # This method doesn't return anything 
    def for_each(self, fn):
        pass
    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # use a queue
        q = Queue()
        # start queue with root node
        q.enqueue(node)
        # while loop that checks size of queue
        while q.size >0:
        # pointer variable that updates at the beginning of each loop
            currentnode = q.dequeue()
            print(currentnode.value)
            if currentnode.left:
                q.enqueue(currentnode.left)
            if currentnode.right:
                q.enqueue(currentnode.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # use a stack
        stack = Stack()
        # start your stack with root node
        stack.push(node)

        # while loop that checks stack size
        while stack.size >0:
            currentnode = stack.pop()
            print(currentnode.value)
            if currentnode.left:
                stack.push(currentnode.left)
            if currentnode.right:
                stack.push(currentnode.right)
    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_print(self):
        pass
    # Print Post-order recursive DFT
    def post_order_print(self):
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
bst.bft_print()
bst.dft_print()
print("elegant methods")
print("pre order")
bst.pre_order_print()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_print()