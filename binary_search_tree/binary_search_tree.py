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
from collections import deque
from typing import Optional

class BSTNode:
    # A node has a value which is an int and two children which are nodes
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    # Insert the given value into the tree
    def insert(self, insert_value: int):
        new_node: BSTNode = BSTNode(insert_value)
        # if root is empty, put in root
        if self.value is None:
            self.value = insert_value
        # if root is bigger than value, search left
        elif insert_value < self.value:
            # if left child is empty, put there
            if self.left is None:
                self.left = new_node
            else: 
                self.left.insert(insert_value)
        # if root is less than value, search right 
        elif insert_value >= self.value: 
            # if right child is empty, put there 
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(insert_value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target: int) -> bool:
        # self will be the root
        # compare self to target 
        # case where we find it 
        if target == self.value:
            return True
        elif target < self.value:
            # return False if dead end 
            if not self.left:
                return False 
            return self.left.contains(target)
        # right side of tree 
        else:
            # return False if dead end
            if not self.right:
                return False 
            return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self) -> int:
        # for null case 
        if self.value is None:
            return None
        # for size of one
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on itself and then recurse down in order 
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        
    def breadth_first_for_each(self, fn):
        queue = deque()
        # add root node
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            fn(current.value)

    # helper function to compose print functions of various traversal methods, prints current node value 
    def print_node(self, node):
        print (node) 
    # Part 2 -----------------------

  

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # functional composition instead of re-writing similar code (below)
        self.breadth_first_for_each(self.print_node)

        # alternative version 
        # queue = deque()
        # queue.append(self)

        # while len(queue) > 0:
        #     current = queue.popleft()
        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
        #     print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # functional composition instead of re-writing almost identical to for each (below)
        self.for_each(self.print_node)
        # print(node.value)  
        # if node.left:
        #     self.left.pre_order_dft(node.left)
        # if node.right:
        #     self.right.pre_order_dft(node.right)

    """
        These 3 below are just the same function calls but with
        the print in a different order 


    """

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.right.in_order_print(node.right)

    # Print Pre-order recursive DFT
    # Go Root > Left > Right recursively
    def pre_order_dft(self, node):
        print(node.value)  
        if node.left:
            self.left.pre_order_dft(node.left)
        if node.right:
            self.right.pre_order_dft(node.right)
    # alternative version below that is less elegant but more resource efficient 
    #     result = []
    #     if node:
    #         result.append(node.value)
    #         result = result + self.pre_order_dft(node.left)
    #         result = result + self.pre_order_dft(node.right)
    #     print(*result, sep='\n')

    # Print Post-order recursive DFT
    # Go Left, Right, Root recursively 
    def post_order_dft(self, node):  
        if node.left:
            self.left.post_order_dft(node.left)
        if node.right:
            self.right.post_order_dft(node.right)
        print(node.value)

    #     result = []
    #     if node:
    #       result = result + self.pre_order_dft(node.left)
    #       result = result + self.pre_order_dft(node.right)
    #       result.append(node.value)
      #   print(*result, sep='\n')
        
   
