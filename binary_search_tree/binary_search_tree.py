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
        print("-- - -- - - -- - -")
        print(self.value)
        print(self.left.value)
        print(self.right.value)

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

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

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
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

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
