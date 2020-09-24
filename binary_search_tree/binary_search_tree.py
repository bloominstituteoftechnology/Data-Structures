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

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        print("target", target)
        print("self.value", self.value)

        if self.value == target:
            print(f"Made it with {target}")
            return True
        elif target < self.value and self.left:
            self.left.contains(target)
        elif target > self.value and self.right:
            print("hitting here?")
            self.right.contains(target)

        return False

        # def contains(self, target):
        # # check if the node is == target
        # if self.value == target:
        #     # if true return true
        #     return True
        # # otherwise check if target is < node value
        # elif target < self.value:
        #     # if left is None, target doesn't exist in tree, return false
        #     if self.left == None:
        #         return False
        #     # if left value is = target return true
        #     elif self.left.value == target:
        #         return True
        #     # otherwise move down left, call contains on left node
        #     else:
        #         self.left.contains(target)
        # # otherwise check if target is >= node value
        # elif target > self.value:
        #     # if right is None, target doesn't exist in tree, return false
        #     if self.right == None:
        #         return False
        #     # if right value is = target return true
        #     elif self.right.value == target:
        #         return True
        #     # otherwise move down right, call contains on right node
        #     else:
        #         self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        current_max = self.value
        current_node = self

        while current_node is not None:
            current_max = current_node.value
            current_node = current_node.right

        return current_max

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
# bst = BSTNode(1)

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
