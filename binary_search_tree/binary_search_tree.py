# import sys
from queue import Queue
from stack import Stack

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
        if  value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
            
    # Return True if the tree contains the value
    # False if it does not
    # Push calls onto the stack until we hit base case & then return up the stack.
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target) # need to return the value hence return used.
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    # Anything to the right is larger.
    # If nothing exists to the right, current(self) is the largest.
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # value is not optional, would need to check for nil otherwise.
        # 5.for_each(fn)
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)  # work through left side of nodes and append values.
        if self.right is not None:  # check right side as we work through the stack.
            self.right.for_each(fn)  # append values to test array if value is not none.

    # recursion is is essentially LIFO.
    # def iter_depth_first_for_each(self, fn):
    #     # depth first traversal order is LIFO
    #     stack = []
    #     # add the first node
    #     stack.append(self)
    #     # continue traversing until stack is empty
    #     while len(stack)>0:
    #         # pop off the stack
    #         current_node = stack.pop()
    #         # add its childmen to the stack
    #         # add right child first and then left child
    #         # to ensure left is popped off first
    #         if current_node.right:
    #             stack.append(current_node.right)
    #         if current_node.left:
    #             stack.append(current_node.left)
    #         # call the fn on self.value
    #         fn(self.value)

    # def iter_breadth_first_for_each(self, fn):
    #     # breadth first traversal follows FIFO
    #     # initialize a queue
    #     # note: this can be done recursivallly but it is complex and generally not worth effort.
    #     q = Queue()
    #     # add the first node
    #     q.append(self)

    #     while len(q)>0:
    #         # current_node = q.deque()
    #         if current_node.left:
    #             q.append(current_node.left)
    #         if current_node.right:
    #             q.append(current_node.right)
    #         fn(self.value)   

    # Part 2 -----------------------

    # Traversals look at each item in the tree, while Searches look for something specific. 
    # DFT = depth first traversal i.e. go as deep as posible down one path b4 other path(s)

    # Print all the values in order from low to high   
    # Hint:  Use a recursive, depth first traversal
    # left most node is always the lowest.   
    def in_order_print(self, node):
    # coded to the test, but not the best way:

        # # base case
        # if node is None:
        #     return
        # self.in_order_print(node.left) # recursive case
        # # if node.left is None:
        # if node.value is not 7:
        #     print(node.value)
        # # if node.right is not None:     
        # #     print(node.value)
        # self.in_order_print(node.right) # recursive case
        # if node.right is None and node.left is not None:
        #     if node.value is not 8:
        #         print(node.value) 

    # Below is much simpler and flexible:

        # base case 
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue
        q = Queue()
        # start queue with root node
        q.enqueue(node)
        # while loop that checks size of queue
        while q.size >0:
        # pointer variable that updates at the beginning of each loop
            currentnode = q.dequeue()
            print(currentnode.value)
            if currentnode.left:
                q.enqueue(currentnode.left)
            if currentnode.right:
                q.enqueue(currentnode.right)

    # # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack
        stack = Stack()
        # start your stack with root node
        stack.push(node)

        # while loop that checks stack size
        while stack.size >0:
            currentnode = stack.pop()
            print(currentnode.value)
            if currentnode.left:
                stack.push(currentnode.left)
            if currentnode.right:
                stack.push(currentnode.right)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
