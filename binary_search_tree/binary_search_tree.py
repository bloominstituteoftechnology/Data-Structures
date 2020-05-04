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
        # #base case: we found a parking spot!
        # # we're in an empty spot in the tree
        # if self is None:
        #     self = BinarySearchTree(value)
        # # if we aren't at the base case, move towards it
        # else:
        #     if value < self.value:
        #         self.left.insert(value)
        #     else:
        #         self.right.insert(value)
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
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        
        print(node.value)
        
        if node.right:
            self.in_order_print(node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.size > 0:
            current_node = queue.dequeue()
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.size > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            print(current_node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        
        if node.left:
            self.pre_order_dft(node.left)

        if node.right:
            self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)
        
        print(node.value)
        
