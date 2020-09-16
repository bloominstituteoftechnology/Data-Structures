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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare the input value with the value of the node
        # if the value < than nodes value
        if value < self.value :
            # We need to go left
            # if we see that there is no left child
            if self.left is None:
                #then we can wrap the value 
                #value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child 
            else: 
                # call the left child's 'insert' method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else: 
            # we need to go right 
            # if we see there is no right child,
            if self.right is None:
            #  then we can wrap the value
            # in a BTSNode and park it there.
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
            # call the right child's 'insert' Method
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value:	        
        #     return True	           
        # if target < self.value:	        	            
        #     if self.left is None:	            
        #         return False	                
        #     else:	            
        #         return self.left.contains(target)	                
        # else:  	         
        #     if self.right is None:	            
        #         return False	               
        #     else:	            
        #         return self.right.contains(target) 
        
        # if the target is equal to the current node
        if target == self.value:
            return True

        elif self.value > target:
            if self.left.value == target:
                return True
            elif self.left is None:
                return False
            elif self.left.value > target or self.left.value < target:
                return self.left.contains(target)

        elif self.value < target:
            if target == self.right.value:
                return True
            elif self.right is None:
                return False

            elif self.right.value > target:
                return self.left.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        # the max is going to be the rightmost value as per the way binary search trees work.
        
        if not self.right:
            return self.value
        
        # otherwise, call get max on the right side.
        return self.right.get_max()

        # # iterative       
        # current_max = self.value
        # # keep a 'current' pointer to keep track of where
        # # we are in the tree
        # current = self

        # while current is not None:
        #     if current.value > current_max:
        #         current_max = current.value
            
        #     current = current.right
        
        # return current_max

            
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the anonymous function on 'self.value'
        fn(self.value)

        # if this node has a left child
        if self.left:
            # pass the anonymous function to it
            self.left.for_each(fn)

        # if this node has a right child
        if self.right:
            # pass the anonymous function to it
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self,fn):
        # DFT: LIFO (last in first out)
        # well use a stack
        stack = []
        stack.append(self)

        # so long as our stacks has nodes in it
        # there's not more nodes to traverese
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()

            # popping from right to left
            # add the current node's right child first
            if current.right:
                stack.append(current.stack)

            if current.left:
                stack.append(current.left)

            # call the anonymous function
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn): #going from right to left like with straight lines
        # breadth-First is first in first out
        # we'll use a queue data structure to facilitate ordering
        queue = deque()
        queue.append(self)

        # continue to traverese so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # instantiate a queue
        queue = deque()
        queue.append(self)
        
        while len(queue) > 0:
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # instantiate a stack
        stack = []
        # push our starting node (self)
        stack.append(self)

        # while the stack is not empty
            # pop the current node
            # print the nodes value
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.right:
               stack.append(current.right)

            if current.left:
                stack.append(current.left)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):

        if self:
            print(self.value)

        if self.left:
            self.left.pre_order_dft()
        
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):

        if not self:
            return
        if self.left:
            self.left.post_order_dft()
        
        if self.right:
            self.right.post_order_dft()
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

bst.in_order_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
