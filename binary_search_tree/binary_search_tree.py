# from dll_stack import Stack
# from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, passed_in_value):
        # if the passed in value is less than the node
        if passed_in_value < self.value:
            # if there is no less than node
            if self.left == None:
                # make a node
                self.left = BinarySearchTree(passed_in_value)
            # if there is a node there
            else:
                # be recursive
                self.left.insert(passed_in_value)
        # if the passed in value is greater than the node
        else:
            # if there is no greater than node
            if self.right == None:
                # make a node
                self.right = BinarySearchTree(passed_in_value)
            # if a node already exists
            else:
                # be recursive
                self.right.insert(passed_in_value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if current value is right, return true
        if target == self.value:
            return True
        # if target is less than current value
        elif target < self.value:
            # if there is no left node, return false
            if self.left == None:
                return False
            # if there is a left node
            else:
                self.left.contains(target)

        # if target is greater than current value
        else:
            # if there is no right node, return false
            if self.right == None:
                return False
            # if there is a right node
            else:
                self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is nothing in the greater than node
        if self.right == None:
            # return current value
            return self.value
        # if there is something in the greater than node
        else:
            # call function on greater than node
            self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call cb on present value
        cb(self.value)
        # if there is a left node, call method on that node
        if self.left:
            self.left.for_each(cb)
        # if there is a right node, call method on that node
        if self.right:
            self.right.for_each(cb)

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
