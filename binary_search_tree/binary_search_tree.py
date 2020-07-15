"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

O(log n): halving with every single iteration

Left Child must be < Parent
Right Child must be > Parent
Note: Keep hierarchy in mind; rule applies throughout tree

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

    
    def insert(self, value):
        """
        Insert the given value into the tree
        """
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see there is no left child,  
            if self.left is None:
                # then we can wrap the value in a BSTNode and 
                # park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's `insert` method
                self.left.insert(value)
        # otherwise, value >= Node's value
        if value >= self.value:
            # we need to go right
            # if we see there is no right child,
            if self.right is None:  
                # then we can wrap the value in a BSTNode and 
                # park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    def contains(self, target):
        """
        Return True if the tree contains the value
        False if it does not
        """
        # Compare input value with value of the node
        # if value == Node's value
        if target == self.value:
            # return True
            return True
        else:
            # if value < Node's value
            if target < self.value:
                # if there is no right child
                if self.left is None:
                    # tree does not contain value
                    return False
                else:
                    # call the left child's `contains` method
                    return self.left.contains(target)
            # if value > Node's value
            if target > self.value:
                # if there is no right child
                if self.right is None:
                    # tree does not contain value
                    return False
                else:
                    # call the right child's `contains` method
                    return self.right.contains(target)
        
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

    # Print the value of every node, starting with the 
    # given node, in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the 
    # given node, in an iterative depth first traversal
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

if __name__ == "__main__":
    
    root = BSTNode(5)

    root.insert(2)
    root.insert(3)
    root.insert(7)
    root.insert(6)
    print(root.left.right.value) #> 3
    print(root.right.left.value) #> 6

    # breakpoint()

    root.insert(2)
    root.insert(3)
    root.insert(7)
    print(root.contains(7)) #> True
    print(root.contains(8)) #> False

    # breakpoint()