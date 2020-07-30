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
        # Take the current value of our node (self.value)
        # Compare to the new value we want to insert
        
        if self < self.value:
        # if new value < self.value
            if not self.left:
            # if self.left is already taken by a node
                if not self.left:
                    self.left = BSTNode(value)
                # make that node call insert()
                else:
                    self.left.insert(value)
            # set the left child to the new node with new value
            
                # the new value is greater than the current node
                # go right
            else:
                if not self.right:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
            
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value >= target
        if self.value < target:
            # check the left subtree (self.left.contains(target))
            if self.left is None:
                return False
            found = self.left.contains(target)
            # if you cannot go left, return False
            
        # if current value < target
        if self.value >= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # if we can go right, go right
        # return when we can't go right anymore
        if not self.right:
            return self.value
        max_value = self.right.get_max()

        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self == None:
            return

        # call the function
        fn(self.value)

        # if left is not None, go left
        if self.left:
            self.left.for_each(fn)

        # if right is not None, go right
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

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
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BinarySearchTree(1)

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
