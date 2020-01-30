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
        if value >= self.value:
            if self.right==None:
                self.right=BinarySearchTree(value) 
            else:
                return self.right.insert(value)
        elif value<self.value:
            if self.left==None:            
                self.left=BinarySearchTree(value)
            else:
                return self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target==self.value:
            return True
        elif target>self.value:
            if self.right!=None:
                return self.right.contains(target)
        elif target<self.value:
            if self.left!=None:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right==None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left!=None and self.right!=None:
            return (self.left.for_each(cb),self.right.for_each(cb))
        if self.left!=None and self.right==None:
            return self.left.for_each(cb)
        if self.left==None and self.right!=None:
            return self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        current = node
        if current.left:
            self.in_order_print(current.left)
        print(current.value)
        if current.right:
            self.in_order_print(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        current = node
        stack = Stack()
        stack.push(current)
        while stack.len() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.right:
                stack.push(popped.right)
            if popped.left:
                stack.push(popped.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # if self.left:
        #     self.left.for_each(cb)
        # cb(self.value)
        # if self.right:
        #     self.right.for_each(cb)
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass