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
        self.count = 1

    # Insert the given value into the tree
    def insert(self, value):
        # Is the value less than the current node's value?
        if value < self.value:
            # insert to the left
            if self.left == None:
                # No "left" child, insert the new node here
                self.left = BSTNode(value)
                return
            else:
                # a "left" child exists, invoke the the child's insert method
                self.insert(value)
                return
        
        # Is the value equal to the current node's value?
        if value == self.value:
            # Increment the node's count
            self.count = self.count + 1
            return 

        # Is the value greater than the current node's value?
        if value > self.value:
            # insert to the right
            if self.right == None:
                # No "right" child, insert the new node here
                self.right = BSTNode(value) 
            else: 
                # a "left" child exists, invoke the the child's insert method
                self.insert(value)
        
        return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Is this the target node?
        if self.value == target:
            return True

        # Not the target node, is the target less than the current node?
        if target < self.value:
            # Are there any "left" nodes to search?
            if self.left == None:
                # No more nodes to search -> the target is not found
                return False

            # A left node or sub-tree exists, return an invocation
            #   of the contains method on the left child node
            return self.left.contains(target)

        # Not the target node, is the target greater than the current node?
        if target > self.value:
            # Are there any "right" nodes to search?
            if self.right == None:
                # No more nodes to search -> the target is not found
                return False

            # A right node or sub-tree exists, return an invocation
            #   of the contains method on the right child node
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Does the node have a "right" child
        #  (if so, that node value is greater than the current node)
        if self.right == None:
            # No right child, this node's value is the max value
            return self.value

        # A right node exists, return an invocation of the 
        #   get_max method on the right child node
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call the function on this node's value
        fn(self.value)

        # Does this node have a "left" child?
        if self.left != None:
            # A left child exists; invoke the for_each method on that child
            self.left.for_each(fn)

        # Does this node have a "right" child?
        if self.right != None:
            # A left child exists; invoke the for_each method on that child
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Does this node have a "left" child?
        if self.left != None:
            # A "left" child exists, invoke the in_order_print on
            #    the left child
            self.left.in_order_print()

        # Exhausted the left children, now print this node
        print(self.value)

        # Does this node have a "right" child?
        if self.right != None:
            # A "right" child exists, invoke the in_order_print on
            #    the right child
            self.left.in_order_print()

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
