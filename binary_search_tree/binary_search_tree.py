from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

          # LEFT CASE
        # check if our new nodes value is less than the current nodes value
            # does it have a child to the left?
                # place our new node here
            # otherwise
                # repeat process for the left

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
            # does it have a child to the right?
                # place our new node here
            # otherwise
                # repeat the process for the right

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
            if self.right is None:
                return self.value
            else:
                return self.right.get_max()
         # base case
        # if empty tree
            # return none

        # recursive case
        # if there is no right value
            # return the root node value
        # otherwise
            # return get max of the right hand child

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
           self.left.for_each(cb)
        if self.right is not None:
           self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left is not None:
           self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        if node is None:
            return
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            node = q.dequeue()
            print(node.value)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
          return
        s = Stack()
        s.push(node)
        while s.size > 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)
