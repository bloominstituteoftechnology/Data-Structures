import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert value into tree
    def insert(self, value):
        if value < self.value:
            # go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if tree contains value, else False
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else: # Target is >= self.value
            # go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)


    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # call this function on the value of each node
    # recursive or iterative approach okay
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        current = self
        storage.push(current)
        while storage.len() > 0:
            current = storage.pop()  # call the pop fn
            print(current.value)
            if current.left:
                storage.push(current.left)
            if current.right:
                storage.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
