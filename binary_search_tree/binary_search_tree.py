# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to current node / if smaller go left / if bigger go right
        # if we reach a leaf , make the new node at that spot

        if value >= self.value:  # compares current value to current node
            if self.right is not None:  # check to see if the right branch is empty
                # recurse, runs the insert func again if right value is not empty,
                self.right.insert(value)
                # using that value as the new base value
            else:
                # sets value to the right as current value if the right value is empty
                self.right = BinarySearchTree(value)

        if value < self.value:
            # please see above
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Check to see if the target value is included in the B_S_T
    def contains(self, target):
        if target == self.value:  # if target is the same as the value, no need to run full func
            return True

        if target >= self.value:  # is the target is greater than the current value move to the right
            if self.right is not None:  # if the right is not none, recurse, run the function again
                return self.right.contains(target)
            else:  # if the right branch is empty return false
                return False
        if target < self.value:  # please see above
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):  # literally just need to keep going right until you cant anymore,
        if self.right is None:
            return self.value
        else:  # this recurses the function and keeps running if you can go right again
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)  # calls function on value of each
        if self.left is not None:  # if the left branch contains a value move there and run again
            self.left.for_each(cb)  # revurses through and runs again
        if self.right is not None:  # please see above
            self.right.for_each(cb)
        else:
            return None

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

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
