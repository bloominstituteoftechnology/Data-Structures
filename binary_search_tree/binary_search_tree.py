import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.position = Queue()
        self.list = []

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target:
            if self.value == target:  
                return True
            if self.value > target:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False 
        else:
            return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # def for_each(self, cb):
    #     return self.find()

    # def find(self):
        
    #     if self.right:
    #         self.list.append(self.right.value)
    #         return self.right.find()

    #     if self.left:
    #         self.list.append(self.left.value)
    #         return self.left.find()
    def for_each(self, cb):
        print(self.value)
        cb(self.value)
        if self.left:
            print('left')
            self.left.for_each(cb)
        if self.right:
            print('right')
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

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
