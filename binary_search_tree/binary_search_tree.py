from collections import deque
from queue import Queue
from stack import Stack

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
        # left case?
        # check if the value is less than the root value?
        if value < self.value:
            # move to the left and check if it is none?
            if self.left == None:
                # insert node here
                new_node = BSTNode(value)
                self.left = new_node
            # otherwise
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # right case?
        if value >= self.value:
            # otherwise
            # move to the right and check if it is none?
            if self.right == None:
                # insert the node here
                new_node = BSTNode(value)
                self.right = new_node
            # otherwise
            else:
                # call insert on the root's right node
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if the node is == target
        if self.value == target:
            # if true return true
            return True
        # otherwise check if target is < node value
        elif target < self.value:
            # if left is None, target doesn't exist in tree, return false
            if self.left == None:
                return False
            # if left value is = target return true
            elif self.left.value == target:
                return True
            # otherwise move down left, call contains on left node
            else:
                self.left.contains(target)
        # otherwise check if target is >= node value
        elif target > self.value:
            # if right is None, target doesn't exist in tree, return false
            if self.right == None:
                return False
            # if right value is = target return true
            elif self.right.value == target:
                return True
            # otherwise move down right, call contains on right node
            else:
                self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right == None:
            return self.value
        else:
            max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # run the function passing in the value of the node
        fn(self.value)

        # if left is not none run for each on left
        if self.left:
            # call function on left
            self.left.for_each(fn)

        # if right is not None run for each on right
        if self.right:
            # call function on right
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # base case
        # if there are no more nodes
        if self == None:
            # return
            return self

        # if there is a node to the left
        if self.left is not None:
            # call in order print on the left
            self.left.in_order_print()
        # print the value of the current node (self.value)
        print(self.value)

        # if there is a node to the right
        if self.right is not None:
            # call order print on the right
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):  # use a queue
        # create a queue
        values = Queue()
        # eneque the first node(self)
        values.enqueue(self)

        # while there is data on queue
        while values.size > 0:
            # dequeue from queue on to current_node
            self = values.dequeue()
            # print the current_node's value
            print(self.value)
            # if the current_node has a left child
            if self.left:
                # enqueue the left child
                values.enqueue(self.left)
            # if the current_node has a right child
            if self.right:
                # enqueue right child
                values.enqueue(self.right)
            # this increases our values.size
            # continuing the loop until done

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):  # use a stack
        # instantiate stack
        values = Stack()
        # push starting node
        values.push(self)
        # while stack is NOT empty:
        while values.size > 0:
            # pop the node
            # print node.value
            self = values.pop()
            print(self.value)
            # if node.left:
            # push left node
            if self.left:
                values.push(self.left)
            # if node.right:
                # push right node
            if self.right:
                values.push(self.right)

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

bst.bft_print()
bst.dft_print()

print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
print("in order")
bst.in_order_print()
# print("post order")
# bst.post_order_dft()
