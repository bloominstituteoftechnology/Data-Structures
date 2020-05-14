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
        ### Notice no return values, because we don't need to send anything up
        ### to original caller. Insert call isn't returning anything.
        #
        # Check if incoming node's value is less than the current node's value
        if value < self.value:
            # we know we need to go left
            # how do we know when we need to recurse again
            # or when to stop?
            if not self.left:
                # we can part our value here
                self.left = BSTNode(value)
            else:
                # we can't park here
                self.left.insert(value)
        else:
            # we know we need to go right
            if not self.right:
                # we can part our value here
                self.right = BSTNode(value)
            else:
                # we can't park here
                self.right.insert(value)

    # def insert(self, value):
    #     if self.value is None: 
    #         head = BSTNode(value) 
    #         self.value = head.value 
    #     if self.value > value:
    #         if self.left is None:
    #             self.left = BSTNode(value)
    #         else:
    #             self.left.insert(value)
    #     else:
    #         if self.right is None:
    #             self.right = BSTNode(value)
    #         else:
    #             self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # When we start searching, self will be the root
        # compare the target against self
        #
        # criteria for returning False: we need to go either left 
        # or right, but there isn't another value in thar dir
        if target == self.value:
            # When this happens, the return True cascades up
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # we'll keep going right until there are no more nodes on the right side
        if not self.right:
            return self.value
        # Otherwise, keep going right
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on the value at this node
        fn(self.value)

        # pass this function to the left child
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child
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

n = [n for n in range(10)]

test = BSTNode(17)
test.insert(35)
test.insert(5)
test.contains(5)
test.get_max()