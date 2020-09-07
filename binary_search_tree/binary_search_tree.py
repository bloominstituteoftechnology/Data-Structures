"""

Binarry search runs on  O (log n ) 
--> This is pretty fast.
---> Binary search only kicks in  after getting more than two nodes in a list
--> Until we see this it is going to run at the same speed.


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
        #Check to see if the value is greater or equal to self.value
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
        #If it is and there is a right side of the binaty search tree available we will insert there. 
        #Otherwise we will create a right, with the value of a new node.
            else:
                new_node = BSTNode(value)
                self.right = new_node

            
            # If the value  is not greater or equal than we will need to  creat a left
            # We will first check if there is  a left and  if so  we  will  insert there
            else: 
                if self.left is not None: 
                    self.left.insert(value)
                #Otherwise we will create  a self.left with  the nodes value.
                    else: 
                        new_node = BSTNode(value)
                        self.left = new_node



     
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target >= self.value:
            if self.right is not None:  
                return self.right.contains(target)
            else: 
                return False
            #That takes care of all of the right side.
        else:
            if self.left is not None: # If we  have  a left child
                return self.left.contains(target)

            else:
                return False
            
        
    

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
