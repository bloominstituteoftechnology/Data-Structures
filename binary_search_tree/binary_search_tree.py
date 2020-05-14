from bst_queue import Queue
from bst_stack import Stack

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
        # if the value is less than the node's value
        if value < self.value:

            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:

                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    def iterative_get_max(self):
        current_max = self.value

        current = self

        while current is not None:
            if current.value > current_max:
                current_max = current.value
            # update the current_max variable if we see a larger value
            current = current.right

        return current_max

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def iterative_for_each(self, fn):
        stack = []

        # add the root node
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # if there is a node check for a left node with recursion
    # if not a left recurse to the right.
    # if there is a left recurse to the end
    # when left is None print the result
    # bubble back up

    # checking for left , if not left print current value - 1
    # recurse to the right, again checking left.
    # while there is a left keep recursing to the left
    # When left is None [8 - left - 5 left - 3 - left - 2 - left - None]
    # print out 2
    # back to 3 which has no more left
    # print out 3
    # recurse to the right which is 4 and 4 has no children
    # print out 4
    # bubble back up to 5 - which no longer has a left
    # print out 5
    # then recurse to the right - which is 7
    # check left, 7 has a left child - recurse to left
    # child value is 6 with no descendants
    # print out 6
    # bubble back up to 7 with ni children
    # print out 7
    # bubbles back up tp up to 8 which is last remaining node, no decendants

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while len(queue) > 0:
            current = queue.dequeue()
            if current is None:
                return
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()

        stack.push(self)

        while len(stack) > 0:
            current = stack.pop()
            if current is not None:
                print(current.value)
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
