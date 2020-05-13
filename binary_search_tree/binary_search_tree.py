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
    # A node has a value which is an int and two children which are nodes
    def __init__(self, value: int):
        self.value: int = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    # Insert the given value into the tree
    def insert(self, insert_value: int):
        new_node: BSTNode = BSTNode(insert_value)
        # if root is empty, put in root
        if self.value is None:
            self.value = insert_value
        # if root is bigger than value, search left
        elif self.value > insert_value:
            # if left child is empty, put there
            if self.left is None:
                self.left = new_node
            else: 
                self.left.insert(insert_value)
        # if root is less than value, search right 
        elif self.value <= insert_value: 
            # if right child is empty, put there 
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(insert_value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target: int):
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
    def get_max(self):
        # for null case 
        if self.value is None:
            return None
        # for size of one
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self):
        # for null case
        if self.left:
            self.left.for_each()
        print(self.value)
        if self.right:
            self.right.for_each()

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
