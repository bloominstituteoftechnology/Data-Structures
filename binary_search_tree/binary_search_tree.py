from stack import Stack
from linked_queue import Queue

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
        if value < self.value:
            if self.left is None:
                new_node = BSTNode(value)
                self.left = new_node
            else: 
                self.left.insert(value)
        else:
            if self.right is None:
                new_node = BSTNode(value)
                self.right = new_node
            else:
                self.right.insert(value)
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value and self.left:
            return self.left.contains(target)
        if target > self.value and self.right:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        current = self
        if current is None:
            return
        fn(current.value)
        if current.left:
            current.left.for_each(fn)
        if current.right:
            current.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     if node is None:
    #         return
    #     queue = list()
    #     queue.append(node)
    #     while len(queue) > 0:
    #         print(queue[0].value)
    #         current = queue.pop(0)
    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)

    def bft_print(self, node):
        if node is None:
            return
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     if node is None:
    #         return
    #     stack = list()
    #     stack.append(node)
    #     while len(stack) > 0:
    #         print(stack[-1].value)
    #         current = stack.pop()
    #         if current.left:
    #             stack.append(current.left)
    #         if current.right:
    #             stack.append(current.right)
    
    def dft_print(self, node):
        if node is None:
            return
        stack = Stack()
        stack.push(node)
        while stack.__len__() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

x = bst.contains(7)
print(x)
x = bst.contains(8)
print(x)
# bst.in_order_print(bst)
bst.bft_print(bst)
# bst.dft_print(bst)