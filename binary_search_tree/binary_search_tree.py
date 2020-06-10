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
        
        if self.value is None: # check to see if is none
            self.value = value # assign to new node if was none
        elif value >= self.value: # else if value if equal or greater self.value place right
            if self.right is None: # check to see if right node is none
                self.right = BSTNode(value) # assign to right node if true
            else:
                self.right.insert(value) # else recursion and begin again one node down
        else: # else place on the left
            if self.left is None: # check to seel if left node is none
                self.left = BSTNode(value) # assign to left node if true
            else:
                self.left.insert(value) # else recursion and begin again one node down
        
                
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if base value is target, return true
        if self.value == target:
            return True
        # if self.value is greater than target
        if self.value > target:
            if self.left is not None:
                #recursively check down the left nodes
                return self.left.contains(target)
        elif self.value < target:
            if self.right is not None:
                # recursively check down the right nodes
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # recurse until none
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

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
        pass

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
