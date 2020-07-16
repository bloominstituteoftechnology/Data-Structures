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
        # Case 1: Value is less than self.value
        if value < self.value:
            # If there is no left child, then insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # Else: ????
                # Repeat the process on left subtree
                # self.left.insert(value)
            else:
                self.left.insert(value)

        # Case 2: Value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1: self.value == target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value

        found = False

        if self.value >= target:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            found = self.left.contains(target)
        # Case 3: otherwise
        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # Forget about the left subtree altogether
        # Iterate through the nodes using a loop construct
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def get_max_(self):
        if self.right is None:
            return self.value
        return self.right.get_max_()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

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
