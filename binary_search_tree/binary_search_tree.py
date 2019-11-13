import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # base case, tree of 1 value. If value is > insert right, else left
        if value > self.value:

            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target to root, if it's in the root return, else < go left > go right
        # print(self.value, target)
        if self.value == target:
            # print('returning true')
            return True
        elif self.value < target and self.right:
            return self.right.contains(target)
        elif self.value > target and self.left:
            return self.left.contains(target)
        else:
            return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        #go right all the way
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #visit each node one time
        # iterative solution
        # stack = Stack()
        # stack.push(self)
        # while stack.len():
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

        # recursive solution
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        return cb(self.value)



        

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
