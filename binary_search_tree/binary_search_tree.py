from collections import deque

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

"""
class BSTNode_1:
    def __init__(self, value):
        self.value = value # current nodes value
        self.left = None # if node is smaller than current node
        self.right = None # if node is larger than current node

    # Insert the given value into the tree
    def insert(self, value):
        # check the new nodes value is less than current nodes value
            # if there s not left child already here
                # add the new node to the left
                # create a BST node and encapsulate the value in it then set it to the left
            # otherwise call insert on the left node
        # otherwise (the new nodes value is greaterthan or equal to the current nodes value)
            # if there is no right child already here
                # add the new node to the right
            # otherwise 
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        # check whether new node's value is greater than or equal to cuu=rr node's value
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check whether curr node matches target
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # check for empty tree
            # return None

# ------------------------------------------------
        # recursive approach
        # CHECK IF THERE IS NO NODE TO THE RIGHT
            # return the nodes value
        # return a call to get the dmax on the right child
# -------------------------------------------------
        # iterative approach

        # initialize the max value

        # get a ref to the current node
        
        # loop while there is still a current node
            # if the current value is greater than the max, value update the max value 
            # move on to the nedt right node

        # return the max value

        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

        # recursive solution
        #base case: no right node available
        # recursive step: pass right sub tree to get_max
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn): # fn or cb
        # call the fucntion passing in the current nodes value

        # if there is a node to the left
            # call the function on the left value

        # if there is a node on the right
            # call the function on the right

        if not self:
            return
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
"""


"""
Redo code from flex
"""

class BSTNode:
    def __init__(self, value):
        self.value = value # this is the parent value if the tree
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Left case
        if value < self.value:
            # if there is no left child
            if not self.left:
                # add new node to the left
                # create BSTNode to encapsulate the value in it then set it to the left
                self.left = BSTNode(value) # BSTNode(value) is the value that is being passed in
            else:
                self.left.insert(value) # recursive function
        # Right case
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target): # Finding a target value
        # Base case (target value is found)
        if self.value == target:
            return True
        # Left case
        if target < self.value:
            # Check if there is a left child
            if not self.left:
                return False
            # otherwise
            else:
                # return call containing left target
                return self.left.contains(target)
                # Right child
        else:
            if not self.right:
                return False
            else:
                # return call containing right target
                return self.right.contains(target)

    # Return the minimm value
    def get_min(self): # Just like get_max
        if not self:
            return None
        while self.left:
            self = self.left
        return self.value

    # Return the maximum value found in the tree
    def get_max(self): # Naturally to the right of the tree
        # Recursive ------------------------------------------------
        # Base case
        if not self.right:
            return self.value
        return self.right.get_max()

        # Iterative ---------------------------------------------------
        # While there is a right child
        while self.right:
            # move to the right. Keeps traversing
            self = self.value
        # once there are no right child to traverse, return value
        return self.value

    # Call the function `fn` on the value of each node (DFT)
    def for_each(self, fn): # Also know as cb sometimes
        # call for each passing in the current nodes value
        fn(self.value)
        # if left exist
        if self.left:
            # call for each on the left child
            self.left.for_each(fn)
        # if right exist 
        if self.right:
            # call for each on the right child
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self): # in order they appear
        # base case
        # if there are no more nodes
            # return
        # if there is a node to the left
            # call in order print on the left
        # print the value of the current node
        # if there is a mode to the right
            # call in order print on the right
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    """
    queue
    grab starting node and put it in a queue

    if there are items in the queue
    dequeue what the current node is
    mark as visted
    print the value
    check left
        enqueue the left
    check right
        enqueue the right
    """
    def bft_print(self): # use a queue
        # create a queue
        # enqueue the first node (self)
        
        # while there is data on the queue   
            # dequeue from queue on to current_node
            # print the current_node's value

            # if the current_node has a left child
                # enqueue the left child

            # if the current_node has a right child
                # enqueue right
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self): # use a stack

        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BinarySearchTree(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
