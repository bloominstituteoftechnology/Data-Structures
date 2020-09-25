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
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check for valid insert
        if not self:
            return
        
        # check if value to insert is a duplicate value, and if so inserts on the right
        if value is self.value:
            self.right = BSTNode(value)
        
        # check if value to insert is greater than current node value
        elif value < self.value:
            # if there is no left value to the current node then add the node to be inserted to the left of the current node
            if not self.left:
                self.left = BSTNode(value)
            # if there is a left value to the current node, call insert method on node to the left
            else:
                self.left.insert(value)
        # check if the value to insert is greater than the current node value
        elif value > self.value:
            # if there is no right value to the current node, then insert the new node at the current node's right
            if not self.right:
                self.right = BSTNode(value)
            # otherwise call insert method on the node to the right
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if the current node value is the target value
        if self.value is target:
            return True
        # if the target is greater than the current node value
        elif target > self.value:
            # if there is no node to the right and the target is still larger, then there is no target value in the tree
            if not self.right:
                return False
            else:
                # if there is a node to the right, call contains method on the node to the right
                return self.right.contains(target)
        else:
            # otherwise move down the left side of the tree, and if there is no left node and target is still smaller, then there is no target in the tree
            if not self.left:
                return False
            else:
                # if there is a node to the left, then call contains method on the node to the left
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # base case to return the right most node in the tree
        if self.right is None:
            return self.value
        else:
            # recursive call of get max on the node to the right of the current node
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # function call onthe current node value
        fn(self.value)
        # check for node to the right
        if self.right:
            # call method on the node to the right
            self.right.for_each(fn)
        # check for node to the left
        if self.left:
            # call method on the node to the left
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        
        queue = Queue()
        queue.enqueue(self)
        while queue:
            cur = queue.dequeue()
            print(cur.value)
            if cur.left:
                queue.enqueue(cur.left)
            if cur.right:
                queue.enqueue(cur.right)
        
        # deq = deque()
        # deq.append(self)
        # while len(deq) > 0:
        #     cur = deq.popleft()
        #     print(cur.value)
        #     if cur.left:
        #         deq.append(cur.left)
        #     if cur.right:
        #         deq.append(cur.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()

        stack.push(self)

        while stack:
            cur = stack.pop()
            print(cur.value)
            if cur.left:
                stack.push(cur.left)
            if cur.right:
                stack.push(cur.right)

        # arr = []
        # arr.append(self)
        # while len(arr) > 0:
        #     cur = arr.pop()
        #     print(cur.value)
        #     if cur.left:
        #         arr.append(cur.left)
        #     if cur.right:
        #         arr.append(cur.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


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
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
