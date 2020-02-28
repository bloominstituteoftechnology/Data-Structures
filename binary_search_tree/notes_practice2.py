import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# insert value
# if there is no node at root - contains/find
# compare value to the root
# if value is smaller
    # look left if node exists repeat steps
    # if no node exists, make new one with this value
# if value is greater or equal
    # look right if node exisits repeat steps
    # if no node exists, make new one with this value

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value: # if value is bigger
            if self.left == None: # there's no left node
                self.left = BinarySearchTree(value) #pass through the function again
            else:
                self.left.insert(value) # insert to the left node
        elif self.value < value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif self.value == value:
            return "tree already has value"
        else:
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if not value:
            return False
        if self.value == target:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if not self:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
