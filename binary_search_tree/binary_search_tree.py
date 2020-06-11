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
        if value < self.value: # is this value less than self.value (ROOT)
            if self.left is None: # if left is empty (none)
                self.left = BSTNode(value) # create a new node and put it on the left
            else:
                self.left.insert(value) # otherwise, compare it to the current value and possibly insert on the left
        elif value >= self.value: # is this value greater than or equal to self.value (ROOT)
            if self.right is None: # if right is empty (none)
                self.right = BSTNode(value) # create a new node and put it on the right
            else:
                self.right.insert(value) # otherwise, compare it to the current value and possibly insert on the right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None: # if the right side is None
            return self.value # then that is the highest value
        else: # otherwise keep going
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # call the function
        if self.left is not None: # if it's not none on the left side
            self.left.for_each(fn) # then CALL the function, and pass in fn
        if self.right is not None: # if it's not none on the right side
            self.right.for_each(fn) # then CALL the function, and pass in fn
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # lowest number furthest from left
        if node is None:
            return
        #recursive case
        self.in_order_print(self.left)

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