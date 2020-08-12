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
        # first check if the input value is less than the root.
        if value < self.value:
            # if it is less than the root, check if there is a child
            # to the left
            if self.left:
                # if there is a child to the left, call the insert function
                # on that child
                self.left.insert(value)
            #if the above is false, create the child to the left
            else:
                # assign the left of the root to be the new input node inserted
                self.left = BSTNode(value)
        # if the input fails the first if statement, it automatically
        # must be greater than or equal to the value of the root
        # so we can do the same operation on the right side until
        # we reach a free space to create our node value.
        else:
            # if there is a child to the right
            if self.right:
                # run the insert method on that child
                self.right.insert(value)
            # if there is no child to the right
            else:
                # create the child to the right
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If theres no BST, return false
        if self.value is None:
            return False
        # if the target is equal to the self.value
        elif target == self.value:
            # the target exists
            return True
        # if the target is greater than the value
        elif target > self.value:
            # check for a right child
            if self.right:
                # if there is a right child, run contains on it
                return self.right.contains(target)
            # if there is no right child
            else:
            # then the target is not contained within
                return False
        # if the target is less than the comparison value
        elif target < self.value:
            # check for a left child
            if self.left:
                # run contains on the left child
                return self.left.contains(target)
            # re-assign the comparison value to the left child
            else:
            # run the contains method on that child
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        # if it's not empty then it's automatically a node. check to the right
        # check for a right child
        elif self.right:
            # if there is a right child, run get_max again on that child
            return self.right.get_max()
        # if there is no right child
        else:
        # return the value
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # apply function to first value
        fn(self.value)
        # if theres a left child
        if self.left:
            #recurse through it
            self.left.for_each(fn)
        # if there's a right child
        if self.right:
            # recurse through it
            self.right.for_each(fn)


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
# """
# bst = BinarySearchTree(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
