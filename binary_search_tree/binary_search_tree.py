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
        # Empty tree use case
        if (self.left is None) & (self.right is None):
            if value >= self.value:
                self.right = BSTNode(value)
            else:
                self.left = BSTNode(value)
        elif (value < self.value):
            # value goes to left branch of root
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            # Value goes to the right branch of root
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you cannot anymore
        # return value
        if self.right is None:
            return self.value
        else:
            self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # base case - no children
        if self.left is None and self.right is None:
            return
        # recursive case - 1 or more children
        # go left, call fn(value) for each node
        if self.left:
            self.left.for_each(fn)
        # go right, call fn(value) for each node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # instantiate a Queue
        q = Queue()
        # insert the value
        q.enqueue(self)

        # while length of q is greater than 0
        while q.size > 0:
            # pop off the top
            top = q.dequeue()
            # print it
            print(top.value)
            # if there is a left child
            if top.left:
                # add left child to queue
                q.enqueue(top.left)
            # if there is a right child
            if top.right:
                # add right child to queue
                q.enqueue(top.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack to keep track of nodes we are processing
        # push self into stack
        # if a tree exists
        if self:
            # print the current value (as it's the first traversal)
            print(self.value)
        # if there is a left child
        if self.left:
            # re-run function with left child as root of tree
            self.left.dft_print()
        # if there is a right child
        if self.right:
            # re-run function with right child as root of tree
            self.right.dft_print()
        # while something still in the stack (not done processing all nodes)
            # use existing 'for_each' as a reference for the traversal logic
            # push when we START, pop when a node is DONE
            # and don't forget to call print()

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
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
