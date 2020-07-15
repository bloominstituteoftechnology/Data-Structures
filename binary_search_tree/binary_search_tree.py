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
from DataStructures.queue.queue import Queue
from DataStructures.stack.stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            self.right = BSTNode(value)
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            return self.left.contains(target) if self.left else None
        else:
            return self.right.contains(target) if self.right else None

    # Return the maximum value found in the tree
    def get_max(self, start=None):
        if start:
            current = start
        else:
            current = self
        try:
            if current.right is not None:
                return max(current.value,
                           self.get_max(start=current.right))
            elif current.right is None:
                return current.value
        except AttributeError:
            return None

    # Call the function `fn` on the value of each node
    def for_each(self, fn, node=False):
        if node is False:
            node = self
        if node is not None:
            self.for_each(fn, node.left)
            fn(node.value)
            self.for_each(fn, node.right)
        elif node is None:
            return

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.value, end="\n")
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    @staticmethod
    def bft_print(node):
        queue = Queue()
        queue.enqueue(node)
        visited = Queue()
        while queue:
            current = queue.storage[0]
            visited.enqueue(current)
            queue.dequeue()
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        while len(visited) > 0:
            x = visited.dequeue()
            print(x.value, end='\n')

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    @staticmethod
    def dft_print(node):
        stack = Stack()
        stack.push(node)
        visited = Queue()
        while stack:
            current = stack.storage[-1]
            visited.enqueue(current)
            stack.pop()
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
        while len(visited) > 0:
            x = visited.dequeue()
            print(x.value, end='\n')

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            print(node.value, end="\n")
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value, end="\n")
