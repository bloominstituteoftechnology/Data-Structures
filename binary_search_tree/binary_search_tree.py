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
        ## case 1 : value is less than self.value
        if value < self.value:
            # if there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
             # else insert()
             ## RECURSION!!!!
                self.left.insert(value)

        ## case 2: value is greater than or equal to self.value
        elif value >= self.value:
            # if there is no left child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
             # else insert()
             ## RECURSION!!!!
                self.right.insert(value)
        #pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        #pass

    # Return the maximum value found in the tree
    def get_max(self):
        ## forget about the left subtree
        ## iterate through the nodes using a loop construct
        
        max_value = self.value
        print(f'max value {max_value}')
        if self.right == None:
            print(f"right node{self.right}")
            print(f"MAX VALUE: {max_value}")
            #max_value = self.value
            print("PASSSSSS")
            final_max_value = self.value
            print(f"FINAL MAX VALUE: {max_value}")
            return final_max_value
            
        elif self.right.value > max_value:
            print(f'right node value: {self.right.value}')
            max_value = self.right.value
            print(f'new max value: {self.right.value}')
            self.right.get_max()
        #print(f'final returned max value {final_max_value}')
        #return final_max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        ## recursive solution
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