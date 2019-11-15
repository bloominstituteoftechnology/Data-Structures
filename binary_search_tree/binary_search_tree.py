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
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            try:
                return self.left.contains(target)
            except:
                return False
        elif target > self.value:
            try:
                return self.right.contains(target)
            except:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        try:
            return self.right.get_max()
        except:
            return self.value
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)


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
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            n = q.dequeue()
            print(n.value)
            if n.left is not None:
                q.enqueue(n.left)
            if n.right is not None:
                q.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size >0:
            p=stack.pop()
            print(p.value)
            if p.left is not None:
                stack.push(p.left)
            if p.right is not None:
                stack.push(p.right)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
