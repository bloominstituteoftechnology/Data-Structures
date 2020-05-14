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
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insert(self, value):
    #     if value > self.value:
    #         og_head = self.value
    #         self.value = value
    #         return self.insert(og_head)
    #     else:
    #         if value > self.right:
    #             return self.right.insert(value)
    #         if value < self.left:
    #             return self.left.insert(value)
    #         else:
    #             return self.insert(value)
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # we always start searching at the root
        # compare the target against the self(node)

        #criteria for returning False:
        # we know we need to go in a direction, but we have reached the end, there is nothing there
        
        if target == self.value:
            return True
        if target < self.value:
            #go left if it is a BTSNode
            if not self.left:
                #if we can't go left, then our value isn't here
                return False
            return self.left.contains(target)
        else: 
            #go right
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #max value should always be the head?
        #confused
        current_max = self.value

        if self.right: 
            if current_max >= self.right.value:
                return current_max
            
            if current_max < self.right.value:
                current_max = self.right.value
                return self.right.get_max()
        else:
            return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        self.value = fn(self.value)
        while self.left:
            self.left.value = fn(self.left.value)
            return self.left.for_each(fn)
        while self.right:
            self.right.value = fn(self.right.value)
            return self.right.for_each(fn)
        else:
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
