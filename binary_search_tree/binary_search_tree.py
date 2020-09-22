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
        
        # check if the value is Less than the value of the current node's value 
            # if there's no left child already there
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it and then set it to the Left node
            # otherwise recursively call insert on left node
        # otherwise the value is Greater than or Equal to the value of the current node
            # if there's no right child already there
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it and then set it to the Right node
            # otherwise recursively call insert on right node
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
            # return True
        # check if the target is Less than the value of the current node's value 
            # if there's no left child already there
                # return False
            # otherwise
                # return a call of 'contains' on the Left child passing in the target value
        # otherwise the target is Greater than to the value of the current node
            # if there's no Right child already there
                # return False
            # otherwise
                # return a call of 'contains' on the Right child passing in the target value
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty Tree
            # return None

        # ** EASY - Recursive **
        # check if there is no node to the Right
            # if True return value
        # otherwise return a call to get_max on the Right child

        # ** ITERATIVE approach **
        # initialize the max value //self's value
        # get a ref to the current node
        # Loop while there is still a Node
            # if the current value is greater than the max value, update the max value
            # move onto the next right node

        # return max value
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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
