import sys
from dll_queue import Queue
from dll_stack import Stack

sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting, there must be a root
        # if value is < self.value
        if value < self.value:
            # if not keep going
            if self.left is None:
                self.left = BinarySearchTree(value)
            # make a left node
            else:
                self.left.insert(value)
        # if >= then go right and
        elif value >= self.value:
            # if not keep going
            if self.right is None:
                self.right = BinarySearchTree(value)
            # make a new node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target = self.value. return
        # If not, go left or right depending on value size
        if self.value == target:
            return True
        if self.value < target:
            if self.right:
                return self.right.contains(target)
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists go right
        # otherwise return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # counting first value
        cb(self.value)
        # counting left side
        if self.left:
            self.left.for_each(cb)
        # counting right side
        if self.right:
            self.right.for_each(cb)

        # iterative approach
        # stack = Stack()
        # stack.push(self)
        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # left, right, root
        # starting with an empty node
        if node is None:
            return
        # Starting on the left-side for the lowest value first
        node.in_order_print(node.left)
        print(node.value)
        # Next moving to the right-side right of each tree
        node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        """
        make a queue
        put the root in the queue
        while queue not empty:
            pop head
            if left:
                add left to end
            if right:
                add right to end
        """
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        """
        Plan:
        make stack
        put root in stack
        while stack no empty
            pop out of stack root
            print value
            if left
                add left to stack
            if right
                add right to stack
        """
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # root, left, right
        if node is None:
            return
        print(node.value)
        node.pre_order_dft(node.left)
        node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left, right, root
        if node is None:
            return
        node.post_order_dft(node.left)
        node.post_order_dft(node.right)
        print(node.value)
