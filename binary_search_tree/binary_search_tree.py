from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # make a new bst node with our value
        new_node = BSTNode(value)
        if new_node.value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)
        elif new_node.value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        value = target
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is not None:
                return self.left.contains(value)
        elif value >= self.value:
            if self.right is not None:
                return self.right.contains(value)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is no value to the right of the root node return the root node's value
        if self.right is None:
            return self.value
        # calls function recursively until condition above is met
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self. right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Lowest number is always furthest to the left
        # base case 
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # not using recursion!
        # use a queue
        queue = Queue()
        # start queue with root node
        queue.enqueue(node)
        # while loop that checks size of queue
        # until the queue is empty
        while queue.size > 0:
            # pointer variable that updates 
            # at the beginning of each loop
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
