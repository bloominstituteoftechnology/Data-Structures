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
        # I like to start with the easier inequality
        if value < self.value:
            # I prefer to start the loop with an assumed positive
            if self.left:
                # If there is a node on the left, we call this same insert function
                self.left.insert(value)
            
            else:
                # if there isn't, we add a node
                self.left = BSTNode(value)

        # Now we work on more than equal to
        else:
            if self.right:
                # Again, if there is already a node, call this same function
                self.right.insert(value)
            
            else:
                # Otherwise add a node
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # First we check the node's value
        if self.value == target:
            return True
        
        # is target smaller?
        elif target < self.value:
            # is there a left node?
            if self.left:
                # if so, we call and return contains on it
                return self.left.contains(target)
                
            # if there isn't a left node
            else:
                return False
        
        # is it greater
        else:
            # is there a right node
            if self.right:
                # if so we call and return contains on it
                return self.right.contains(target)
                
            # if there isn't a right node
            else:
                return False
        


    # Return the maximum value found in the tree
    # On a proper BST the bottom right value will always be the largest value
    def get_max(self):
        # we set max value to the node's value
        maxvalue = self.value
        # is there a right node?
        if self.right:
            # if so, then call and return get_max on it
            return self.right.get_max()
        
        # this should recurse all the way though til the end 
        else:
            return maxvalue


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

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
