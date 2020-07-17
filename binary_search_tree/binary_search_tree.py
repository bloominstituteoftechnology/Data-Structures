import sys

from queue import Queue
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        # self.storage = []
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        # return len(self.storage)
        # Start at the head and add one to the count until you reach the tail (.next is None)
        return self.size
    def push(self, value):
        # self.storage.append(value)
        new_node = Node(value)
        # If the list is empty, set the head node and it's .next value to be the value
        if self.head is None:
            self.head = new_node
            # self.head.next = new_node
            self.tail = new_node
        # Otherwise, if there are nodes, change the current tail's .next value from None to the value
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop(self):
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     value = self.storage.pop()
        #     return value
        if self.head is None:
            return None
        elif self.head.next is None:
            removed = self.head
            self.head = None
            self.size -= 1
            return removed.data
        else:
            new_last = self.head
            # While there is at least two elements after the current Node, keep moving through the loop since it isn't the next to last Node
            while new_last.next.next:
                new_last = new_last.next

            removed = new_last.next
            new_last.next = None
            self.size -= 1
            return removed.data
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
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
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

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.put(node)

        while storage.qsize() > 0:
            node = storage.get()
            print(node.value)

            if node.left:
                storage.put(node.left)
            if node.right:
                storage.put(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)

        while storage.size > 0:
            node = storage.pop()
            print(node.values)

            if node.left:
                storage.push(node.left)
            if node.right:
                storage.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
