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
        # Left side
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # RIght side
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check root
        if target == self.value:
            return True
        #check subleft nodes:
        elif target < self.value and self.left:
                return self.left.contains(target) 
        #check subright nodes:
        elif target > self.value and self.right:
                return self.right.contains(target) 

    # Return the maximum value found in the tree
    def get_max(self):
        # check if there is not a right(greater) value
        max_val = self.value 

        if self.right is None:
            return max_val
        # traverse down list until no more right values are found
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive depth first traversal to process function in order
        if self.left is not None:
            self.left.for_each(fn)
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node = None):
        # use previous function for this operation
        if node is None:
            current = self
        else:
            current = node
        
        current.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node= None):
        #allows function to run on itself if no node passed
        if node is None:
            current = self
        else:
            current = node
        queue = [current]

        #check for empty tree
        if current.value is None:
            return 
        
        # Traverse through queue 
        while queue:
                # get queued node
                current = queue.pop(0)
                # printing each node
                print(current.value)
                # add left to queue first for in order approach 
                queue.extend(filter(None, [current.left, current.right]))

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        if node is None:
            current = self
        else:
            current = node

        stack = [current]

        #check for empty tree
        if current.value is None:
            return 
        
        # Traverse through queue 
        while stack:
                # get queued node
                current = stack.pop()
                # printing each node
                print(current.value)
                # add left to stack last to be popped first 
                stack.extend(filter(None, [current.right, current.left]))


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node = None):
        if node is None:
            current = self
        else:
            current = node

        #print root node
        print(current.value)
        #print left node
        if current.left:
            current.left.pre_order_dft()
        #print right node
        if current.right:
            current.right.pre_order_dft()


    # Print Post-order recursive DFT
    def post_order_dft(self, node = None):
        if node is None:
            current = self
        else:
            current = node 

        # print all left
        if current.left:
            current.left.post_order_dft()
        # print all right
        if current.right:
            current.right.post_order_dft()
        #print all root
        print(current.value)
           

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
