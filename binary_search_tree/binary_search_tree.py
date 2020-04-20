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
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a node_queue
        node_queue = Queue()
        # add current node to queue
        node_queue.enqueue(node)
        # while queue is not empty

        while node_queue.size > 0:
            # print(node_queue.size)
            # pop node off queue
            node = node_queue.dequeue()
            # print(node_queue.size)
            # print node
            print(node.value)
            # add its children
            if node.left is not None:
                node_queue.enqueue(node.left)
                # print(node_queue.size)
                # add left (if you can)
            if node.right is not None:
                # add right (if you can)
                node_queue.enqueue(node.right)
                # print(node_queue.size)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node_stack
        node_stack = Stack()
        # push the current node onto stack
        node_stack.push(node)
        # while we have items on the stack
        while node_stack.size > 0:
            # print the current value and pop it off
            node = node_stack.pop()
            print(node.value)
            # push the left value of current node if we can
            if node.left is not None:
                node_stack.push(node.left)
            # push the right value of the current node if we can
            if node.right is not None:
                node_stack.push(node.right)

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