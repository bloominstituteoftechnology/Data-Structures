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


    def insert(self, value):
        # Lower values left
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # Higher values right
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    def contains(self, target):
        if target == self.value:
            return True
        # Check left if lower value
        if target < self.value:
            if self.left:
                return left.contains(target)
            else:
                return False
        # Check right if higher value
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False



    def get_max(self):
        # Higher values are put to the right
        if self.right:
            return self.right.get_max()
        else:
            return self.value


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
        pass
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        # check if we can "move left"
        # visit the node by printing its value
        # check if we can "move right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"​
        # start by placing the root in the queue​
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
            # dequeue item from front of queue
            # print that item
            # place current item's left node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # initialize an empty stack
        # push the root node onto the stack​
        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
            # pop top item off the stack
            # print that item's value​
            # if there is a right subtree
                # push right item onto the stack                
            # if there is a left subtree
                # push left item onto the stack


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
