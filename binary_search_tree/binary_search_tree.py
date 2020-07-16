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
# import sys
# sys.path.append('../queue')
# from queue import Queue
# sys.path.append('../stack')
# from stack import Stack

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
        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    def contains(self, target): 
        if target == self.value:        
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
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        # call function on value
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
            
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(self)

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(self)

    def pre_order_dft(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # visit the node by printing its value
        print(self.value)

        # check if we can "move left"
        if self.left is not None:
            self.left.pre_order_dft(self)

        # check if we can "move right"
        if self.right is not None:
            self.right.pre_order_dft(self)

    def post_order_dft(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.post_order_dft(self)

        # check if we can "move right"
        if self.right is not None:
            self.right.post_order_dft(self)

        # visit the node by printing its value
        print(self.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
    
        while queue.size > 0:
            current_item = queue.dequeue()
            print(current_item.value)

            if current_item.left is not None:
                queue.enqueue(current_item.left)

            if current_item.right is not None:
                queue.enqueue(current_item.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.__len__() > 0:
            top_item = stack.pop()   
            print(top_item.value)

            if top_item.right is not None:
                stack.push(top_item.right)

            if top_item.left is not None:
                stack.push(top_item.left)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1
        return None

    def dequeue(self):
        if self.size != 0:
            item = self.storage[0]
            del self.storage[0]
            self.size -= 1
            return item
        else:
            return None

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()