from collections import deque
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
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if there's no left child
            if self.left is None:
            # then we can wrap the value in the BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there's a child
            else:
            # call left child's insert method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go to this node's right child
            # if there's no right child,
            if self.right is None:
            # value in the BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there's a child
            else:
            # call right child's insert method
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
        """
        if self.right is None and self.left is None:
            return self.value
        current = self
        while current.right:
             current = current.right
        return current.value

    #U: Traverse BST to find global max
    #1: Check your input --> is it None?
        if not self:
            return None
    #2: declare max variable and give self.value
        max = self.value
        current = self
    #3: iterate through the tree
        while current:
    #4: update max value
            if current.value > max:
                max = current.value
    #5: move to the right
            current = current.right
        return max
        """
    # recursive solution
    # base case: no right node
    # recursive step: pass right subtree to get_max
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #U: apply fn to each node of tree
        #1: check if empty
        #2: apply fn to root
        #3: call for_each on left and right subtree
        if not self:
            return
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        """  
        if self is None or self.fn == fn:
            return
        if self.fn < fn:
            return self.right.for_each(fn)
        return self.left.for_each(fn)
        """
    # Part 2 -----------------------

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
        #1: define deque
        #2: add root node to deque
        #3: iterate: while there are items in the deque
        #4: process: dequeue/pop node from deque and print
        #5: add child nodes to deque for processing
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
        # historically uses a stack to keep track of where we are in traversal
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if not self:
            return
        # root -> left -> right
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if not self:
            return
        # left -> right -> root
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

    def in_order_dft(self):
        if not self:
            return
        # left -> root -> right
        if self.left:
            self.left.in_order_dft()
        print(self.value)
        if self.right:
            self.right.in_order_dft()


# This code is necessary for testing the `print` methods

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
bst.in_order_dft()
print("post order")
bst.post_order_dft()
