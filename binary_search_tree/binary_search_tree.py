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
        # check to see if the value is greater than or equal to the value to the left
        if value < self.value and self.left is None:
            self.left = BSTNode(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        elif value >= self.value and self.right is None:
            self.right = BSTNode(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # End Goal to return true: if the target value equals the self.value
        # than the tree contains the value.
        if target is self.value:
            return True

        # If the target is less than the value and the left value is NOT equal
        # to None, than we want to recursively run the contain method on the
        # self.left value.
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        
        # if the target is less than the self.value and the left value is None
        # than that means that the target is not contained in the tree
        elif target < self.value and self.left is None:
            return False

        # if the target is less than or equal to the self.value and the right value
        # is NOT equal to None, than we want to recursively run the contains method on
        # the self.right value
        elif target >= self.value and self.right is not None:
            return self.right.contains(target)

        # if the target is greater than or equal to the self.value and the 
        # right value is None, than the target is not contained in the tree.
        elif target >= self.value and self.right is None:
            return False

            

    # Return the maximum value found in the tree
    def get_max(self):
        # right values always increase in value as you go down the tree.
        # so if we just continue to search down the right, as long as the 
        # self.right is not None, than that value is our Max
        if self.right is None:
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
