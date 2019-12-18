from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        """
        if first element
          place
        if not first element
          compare current with new
            if less, move left
            if greater, move right
        """
        if self.value is None:
            self.value = value
        else:
            if self.value > value:
                if self.left is None:
                    self.left = value  # TODO: need to wrap in something
                else:
                    pass  # TODO: continue the search
            elif self.value < value:
                if self.right is None:
                    self.right = value  # TODO: need to wrap in something
                else:
                    pass  # TODO: continue the search

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.value > target:
                if self.left is None:
                    return False
                elif self.left == target:
                    return True
                else:
                    pass  # TODO: continue the search
            elif self.value < target:
                if self.right is None:
                    return False
                elif self.right == target:
                    return True
                else:
                    pass  # TODO: continue the search

    # Return the maximum value found in the tree
    def get_max(self):
        # get right most value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # recursion might be better
        # need to traverse both sides of tree
        # hit a node, call cb, go to next
        pass

    # DAY 2 Project -----------------------

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

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
bst.insert(4)
bst.insert(6)
print(bst.value)
print(bst.left)
print(bst.right)
