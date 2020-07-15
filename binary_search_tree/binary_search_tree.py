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
        # inserting value into root-less tree
        if self is None:
            self.value = BSTNode(value)
        # general case
        else:
            # inserting a node on the left
            if value < self.value:
                # checking to see if a node already exits there
                if self.left:
                    # recursively insert value
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            # inserting a node on the right
            else:
                # checking to see if a node already exits there
                if self.right:
                    # recursively insert value
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # checking if empty list contains target
        if self is None:
            return False
        # check if root node contains target
        elif self.value == target:
            return True
            
        boolean = False
        # check in which direction the target flows (from the root)
        if target < self.value:
            if self.left is None:
                return False
            boolean = self.left.contains(target)

        else:
            if self.right is None:
                return False
            boolean = self.right.contains(target)
        return boolean

    # Return the maximum value found in the tree
    def get_max(self):
        pass

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


if __name__ == "__main__":
    bst = BSTNode(5)

    bst.insert(2)
    bst.insert(3)
    bst.insert(7)

    print(bst.contains(7))
    print(bst.contains(8))
    