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
# from sys import path
# path.append("../")
from scaffold import Stack, Queue


class BSTNode():                                                           #<<<
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right

    @value.setter
    def value(self, x):
        self._value = x
    @left.setter
    def left(self, x):
        self._left = x
    @right.setter
    def right(self, x):
        self._right = x

    # Insert the given value into the tree
    def insert(self, value):
        if self._value == value:
            return
        elif value <= self._value:
            if self._left:
                return self._left.insert(value)
            else:
                self._left = BSTNode(value)
        else:
            if self._right:
                return self._right.insert(value)
            else:
                self._right = BSTNode(value) 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self._value == target:
            return True
        elif target < self._value and self._left:
            return self._left.contains(target)
        elif target > self._value and self._right:
            return self._right.contains(target)
        return

    # Return the maximum value found in the tree
    def get_max(self):
        if self._right == None:
            return self._value
        else:
            return self._right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self._value)
        if self._left is not None:
            self._left.for_each(fn)
        if self._right is not None:
            self._right.for_each(fn)


    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node._left)
            print(node._value)
            self.in_order_print(node._right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.__len__() > 0:
            n = q.dequeue()
            print(n._value)
            if n._left:
                q.enqueue(n._left)
            if n.right:
                q.enqueue(n._right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.__len__() > 0:
            n = s.pop()
            print(n._value)
            if n._left:
                s.push(n._left)
            if n._right:
                s.push(n._right)
                

    # Stretch Goals -------------------------
    # Note: Research may be required


    # # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node._value)
            self.pre_order_dft(node._left)
            self.pre_order_dft(node._right) 

    # # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node._left)
            self.post_order_dft(node._right)
            print(node._value) 


if __name__ == "__main__": #>>> <PASS>
    pass
