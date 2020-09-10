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

# Test runs okay for first half.
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):	    
        if value < self.value:	       
            if self.left:	          
                self.left.insert(value)            
            else:	            
                self.left = BSTNode(value)	                
        else:	        
            if self.right: 	            
                self.right.insert(value)	                
            else:	           
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:	        
            return True	           
        if target < self.value:	        	            
            if self.left is None:	            
                return False	                
            else:	            
                return self.left.contains(target)	                
        else:  	         
            if self.right is None:	            
                return False	               
            else:	            
                return self.right.contains(target) 
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:	        
            return self.value	            
        else:	        
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)	        
        if self.left:	       
            self.left.for_each(fn)	            
        if self.right:	        
            self.right.for_each(fn)

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
        q = []
        q.append(self)
        while len(q):
            current = q.pop(0)
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)       
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass


    def in_order_dft(self):
        pass


    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

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

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
