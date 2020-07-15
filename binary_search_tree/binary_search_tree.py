"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two parts:
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
        # compare value to parent node

        # if passed in value is less than self.value:
        if value < self.value:
            # check to see if there is a child
            # if not:
            if not self.left:
                # assigng child to a new BSTNode
                self.left = BSTNode(value)
            # else:
                # repeat the process on left subtree
                self.left.insert(value)
            
        # if pass in value is greater than or equal self.value:
        if value >= self.value:
            # check to see if there is a child
            # if not:
            if not self.right:
                # Assign child to new BTSNode
                self.right = BSTNode(value)
            else:
                # repeat process on right subtree
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # check to see if target is self.value
        if target == self.value:        
            # return True
            return True
        # check to see if value is less than self.value
        if target < self.value:
            # check to see if t here is a child to the left
            if not self.left:
                return False
            else:
                # recurse that 
                # the self that's passed in through the contains
                # method is the left node 
                return self.left.contains(target)
        else:
            # if there is not a child to the roit
            if not self.right:
                return False
            else:
                # cirlce cirlce circle     
                return self.right.contains(target)
            

    # Return the maximum value found in the tree
    def get_max(self):
        # look at the node
        # if there isn't a node.right:
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
