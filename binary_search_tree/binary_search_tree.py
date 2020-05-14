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
        if self.value is None: # the value is none 
            root = BSTNode(value) 
            self.value = root.value 
        if self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    #check if the incoming value is less that the current node's value
    # def insert(self, value):
    #     if value < self.value:
    #         # we know we need to go left
    #         # how do we know when we need to recurse again,
    #         # or when to stop?
    #         if not self.left:
    #         # we can park our value here 
    #             self.left = BSTNode(value)
    #         else:
    #             # we can't park here
    #             # keep searching
    #             self.left.insert(value)
    #     else:
    #         #we know we need to go right 
    #         if not self.right:
    #             self.right = BSTNode(value)
    #         else:
    #             self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root 
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there is nothing in the left or right direction 
        if target == self.value: 
            return True
        if target < self.value:
            #go left if left is a BinarySearchTree
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            #go right if right is a BinarySearchTree
            if not self.right:
                return False
            return self.right.contains(target)
            

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max_value

    # def get_max(self):
    #     # we always go right until there are no more nodes on the right side 
    #     if not self.right:
    #         return self.value
    #     #otherwise keep going right
    #     return self.right.get_max()

    # def iterative_get_max(self):
    #     current_max = self.value

    #     current = self

    #     # traverse our structure
    #     while current is not None:
    #         if current.value > current_max:
    #             current_max = current.value
    #         #update our current_max variable if we see a larger value
    #         current = current.right

    #     return current_max

    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # call the fn on the value at this node
    # def for_each(self, fn)
    #     fn(self.value)
    # #pass this function on the left child 
    #     if self.left:
    #     self.left.for_each(fn)
    # #pass this function to the right child 
    #     if self.right:
    #     self.right.for_each(fn)
    


    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            print(current.value)

    # def bft_print(self, node):
    #     to_print = SimpleQueue()
    #     to_print.put(node)
    #     while to_print.qsize() != 0:
    #         self = to_print.get()
    #         if self.left is not None:
    #             to_print.put(self.left)
    #         if self.right is not None:
    #             to_print.put(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node ):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            print(current.value)

    # def dft_print(self, node):
    #     retrace = LifoQueue()
    #     retrace.put(node)
    #     while self.left is not None:
    #         self = self.left
    #     while retrace.qsize() != 0:
    #         self = retrace.get().right
    #         if node is not None:
    #             while self.left is not None:
    #                 retrace.put(node)
    #                 self = self.left
    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)
            

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)
