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
        # compare the input value with the value of the Node.
            # if value < Node's value, we need to go left
            if value < self.value:
                 # if we see that there is no left child
                 if self.left is None:
                    # then we can wrap the value in a BSTNode and park it
                    self.left = BSTNode(value)
                 # otherwise if there is a child
                 else:
                # call the left child's 'insert' method
                    self.left.insert(value)
            # if value >= Node's value, we need to go right
            else:
                # we need to go right if we see there is no right child
                if self.right is None:
                    # then we can wrap the value in a BSTNode and park it
                    self.right = BSTNode(value)
                # otherwise if there is a child
                else:
                    # call the right child's 'insert' method
                    self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value and self.left:
            return self.left.contains(target)

        if self.right:
            return self.right.contains(target)

        return False 

    # Return the maximum value found in the tree
    def get_max(self):
        node = self.right

        while node:
            if node.right:
                node = node.right
            else:
                break

        return node and node.value or self.value

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
bst = BinarySearchTree(1)

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
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
