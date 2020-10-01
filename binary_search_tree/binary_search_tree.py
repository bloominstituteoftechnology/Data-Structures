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
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if self.right == None and self.left == None:
        #     return None

        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # base case
        # if there are no more nodes
            #return
        if self.left == None and self.right == None:
            return
            
        #if there is a node to the left 
        if self.left is not None:
            # call in order print on the left
            self.left.in_order_print()
        # print the value of the current node (self.value)
        print(self.value)
        #if there is a node to the right 
        if self.right is not None:
            # call in order print on the right
            self.right.in_order_print()
       

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    def bft_print(self): #queue
        #create a queue
        queue = Queue()
        queue.enqueue(self)
        
        while queue:
            node = queue.dequeue()
            print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    def dft_print(self): # stack
        stack = Stack()
        stack.push(self)

        while stack:
            node = stack.pop()
            print(node.value)
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # # Print Post-order recursive DFT
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

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
