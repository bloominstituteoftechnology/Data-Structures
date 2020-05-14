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

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if the value is less than the node's value
        if value < self.value:
            # if left is None
            if not self.left:
                # create new left node
                self.left = BSTNode(value)
            else:
                # insert the value on the left
                self.left.insert(value)
        else: # the value is greater than or equal to nodes value
            # if right node is None
            if not self.right:
                # create the new right node
                self.right = BSTNode(value)
            else:
                # insert the value on the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
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

    # Return the maximum value found in the tree
    def get_max(self):
        # check right side because it's at least equal to or greater than current root
        if self.right:
            # if there is a right node, repeat function
            return self.right.get_max()
        else:
            # if there isn't a right node, maximum value has been found
            return self.value

    def iterative_get_max(self):
        current_max = self.value

        current = self
        # traverse our structure
        while current:
            if current.value > current_max:
                current_max = current.value
        # update our current_max variable if we see a larger value
            current = current.right
        return current_max

    # Call the function `fn` on the value of each node
    # recursive depth-first traversal
    def for_each(self, fn):
        fn(self.value)
        # if there is a left node
        if self.left:
            # call for_each
            self.left.for_each(fn)
        # if there is a right node
        if self.right:
            # call for_each
            self.right.for_each(fn)

    # iterative depth-first traversal
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

    # iterative breadth-first traversal
    def breadth_first_for_each(self, fn):
        queue = deque()
        # add the root node
        queue.append(self)
        # loop so long as the stack still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
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
            # when left is None, print the resulting value
            # bubble back up

            # checking for left. if no left, print current value - 1
            # recurse to the right, again checking left.
            # while there is a left, keep recursing to the left
            # when left is None - print value [ 8 - left - 5 - left - 3 - left - 2 - left - None]
            # print out 2
            # back to 3 which has no more left
            # print out 3
            # recurse to the right - which is 4 and 4 has no children
            # print out 4
            # bubble back up to 5 - which no longer has a left
            # print out 5
            # recurse to the right - which is 7
            # check left, 7 has a left child - recurse to left
            # child value is 6 with no descendants
            # print out 6
            # bubble back up to 7 with no children
            # print out 7
            # bubble back up to 8 which is last remaining node, no descendants
            # print out 8.
            # exit function



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
