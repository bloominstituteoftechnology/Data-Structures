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
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            self = BSTNode(value)
        else:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

        # while(value < self.value and self.left or value > self.value and self.right):
        #     if value < self.value:
        #         self = self.left
        #     else:
        #         self = self.right
            
        # if value < self.value:
        #     self.left = BSTNode(value)
        # else:
        #     self.right = BSTNode(value)               

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self is None:
            return False
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

        # if self.value == target:
        #     return True
        # if target < self.value:
        #     if not self.left:
        #         return False
        #     else:
        #         return self.left.contains(target)
        # else:
        #     if not self.right:
        #         return False
        #     else:
        #         return self.right.contains(target)        

    # Return the maximum value found in the tree
    def get_max(self):        
        while self.right:
            self = self.right
        return self.value

        # if not self.right:
        #     return self.value
        # return self.right.get_max()

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
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.storage:
            current_node = q.dequeue()
            print(current_node.value)            
            if current_node.left:
                q.enqueue(current_node.left)            
            if current_node.right:
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while stack:
            current_node = stack.pop()
            print(current_node.value)            
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
