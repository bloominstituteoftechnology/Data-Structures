from collections import deque
from itertools import filterfalse

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
        self.parent = None
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # inserting value into root-less tree
        if self is None:
            self.value = BSTNode(value)
        # general case
        else:
            # inserting a node on the left
            if value < self.value:
                # checking to see if a node already exits there
                if self.left:
                    # recursively insert value
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            # inserting a node on the right
            else:
                # checking to see if a node already exits there
                if self.right:
                    # recursively insert value
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # checking if empty list contains target
        if self is None:
            return False
        # check if root node contains target
        elif self.value == target:
            return True
            
        boolean = False
        # check in which direction the target flows (from the root)
        if target < self.value:
            if self.left is None:
                return False
            boolean = self.left.contains(target)

        else:
            if self.right is None:
                return False
            boolean = self.right.contains(target)
        return boolean

    # Return the maximum value found in the tree
    def get_max(self):
        # intialize root as max value
        max_value = self.value
        # checking if tree root value or
            # self.right is empty
        if self.right is None:
            return self.value
        else:
            max_value = self.right.get_max()

        return max_value

    # Return the minimum value found in tree
    def get_min(self):
        # Get to bottom left node
        min_value = self.value
        # checking if tree root value or
            # self.left is empty
        if self.left is None:
            return self.value
        else:
            max_value = self.left.get_min()

        return min_value  


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # for cases with a single root node
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        arr = []
        cb = lambda x: arr.append(x)

        cb(node.value)

        if node.left:
            node.left.for_each(cb)

        if node.right:
            node.right.for_each(cb)

        arr.sort()
        for val in arr:
            print(val)

             
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Create Queue with initial node inside
        queue = deque([])
        queue.append(node)

        while len(queue) > 0:
            current_node = queue[0]
            print(current_node.value)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            queue.popleft()
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Create Stack with initial node inside
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current_node = stack[-1]

            print(stack.pop().value)

            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)


    # Stretch Goals -------------------------

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            node.left.for_each(print)

        if node.right:
            node.right.for_each(print)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)
            
        print(node.value)
        

if __name__ == "__main__":
    bst = BSTNode(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)

    print("In Order Print")
    bst.in_order_print(bst)
    print("\nBreadth First Print")
    bst.bft_print(bst)
    print("\nDepth First Print")
    bst.dft_print(bst)
    print("\nPre Order Print")
    bst.pre_order_dft(bst)
    print("\nPost Order Print")
    bst.post_order_dft(bst)