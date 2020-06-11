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
from stack import Stack
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # we're gonna go in 
        # if the value < root's value 
        if value < self.value:
            # go left 
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left: 
                # then self.left is a Node 
                # now what?
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value 
        else:
            # go right
            # how do we go right? 
            # we have to check if there is another node on the right side 
            if self.right:
                # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case: Node is equal to target
        if target == self.value:
            return True
        
        # Check left-hand side
        elif target < self.value:
            # Subcase: Nothing to the left of self.value
            # Therefore, target does not exist in tree
            if self.left == None:
                return False
            # Subcase: There are nodes to the left of self.value
            # Recursively check left nodes
            else:
                return self.left.contains(target)

        # Check right-hand side
        else:
            # Subcase: Nothing to the right of self.value
            # Therefore, target does not exist in tree
            if self.right == None:
                return False
            # Subcase: There are nodes to the right of self.value
            # Recursively check right nodes
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # If node is the maximum value in the tree
        if self.right == None:
            return self.value
        # If the node is not the maximum value in the tree
        else:
            return self.right.get_max()
        


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Apply fn to root node
        fn(self.value)
        
        # Recursively apply fn to left-side nodes, if they exist
        if self.left:
            self.left.for_each(fn)
        
        # Recursively apply fn to right-side nodes, if they exist
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
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
