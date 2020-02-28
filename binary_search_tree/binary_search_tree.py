import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # if there is no node at root insert value at root
    # compare value to the root
    # if value is smaller:
    #   look left and if theres already a node, repeat
    #   if there isnt a node, make one with this value
    #
    # if value is bigger:
    #   look right and if theres already a node, repeat
    #   if there isnt a node, make one with this value
    def insert(self, value):
        if value <= self.value:
            # if there is already a node
            if self.left is not None:
                self.left.insert(value)
            else:
                # make a new node with the value
                self.left = BinarySearchTree(value)
        
        elif value >= self.value:
            # theres already a right node
            if self.right is not None:
                self.right.insert(value)
            else:
                # make a new node with the value
                self.right = BinarySearchTree(value)





    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
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
    # DFT Steps:
    # initialize a stack
    # push root to stack
    # while stack not empty
    # pop top item out of stack into temp
    # DO THE THING!!!!!!
    # if temp has right right put into stack
    # if temp has left left put into stack
    def dft_print(self, node):
        s = Stack()
        s.push(self.value)
        while not s.isempty():
            print(s.pop())
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


tree = BinarySearchTree(23)
tree.insert(45)
tree.inset(20)
tree.dft_print()