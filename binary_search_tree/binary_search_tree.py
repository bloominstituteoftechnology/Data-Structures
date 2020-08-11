from collections import deque


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

Tree structures w/ max 2 child nodes. 
Left nodes are less than root. 
Right nodes are greater than root. 

Binary Search?? 
    Cut dataset in half. 
    Ex) arr = [1, 2, 3, 4, 5, 6] | elem = 2, elem = 0  
                [1, 2, 3] 
                [1]
                [] --> not here, if 0 


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
        if value < self.value: 
            if not self.left: 
                self.left = BSTNode(value) 
            else: 
                self.left.insert(value) 
        elif value >= self.value: 
            if not self.right: 
                self.right = BSTNode(value) 
            else: 
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True 
        if target < self.value: 
            if not self.left: 
                return False 
            else: 
                return self.left.contains(target) 
        else: 
            if not self.right:
                return False 
            else: 
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if not self: 
            return None 
        if self.right: 
            return self.right.get_max() 
        else: 
            return self.value

        # if not self: 
        #     return None 
        # max_value = self.value 
        # current = self 
        # while current: 
        #     if current.value > max_value: 
        #         max_value = current.value 
        #     current = current.right 
        #     return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) 
        if self.right is not None: 
            self.right.for_each(fn)
        if self.left is not None: 
            self.left.for_each(fn)

    # Part 2 -----------------------------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return 
        # left -> root -> right
        if self.left:
            self.left.in_order_print()
        
        print(self.value)

        if self.right:
            self.right.in_order_print() 

        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # define deque 
        # add self to deque 
        # iterate: while there are items in the deque 
        # dequeue/pop from deque and point to result, and print 
        # add left and right children to the deque 

        qq = deque() 
        qq.append(self) 

        while len(qq) > 0: 
            current = qq.popleft() 
            print(current.value) 
            if current.left: 
                qq.append(current.left) 
            if current.right: 
                qq.append(current.right)  


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = [] 
        s.append(self) 

        while len(s) > 0: 
            current = s.pop() 
            print(current.value)
            if current.left: 
                s.append(current.left) 
            




    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     # check self 
    #     # print self 
    #     # root -> left -> right 
    #     # recurse to the left 
    #     # recurse to the right 
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     # check self
    #     # left -> right -> root  
    #     # recurse to the left 
    #     # recurse to the right 
    #     # print self 
    #     pass 


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
