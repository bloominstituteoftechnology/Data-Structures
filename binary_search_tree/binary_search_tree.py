from queue import Queue
from stack import Stack
from linked_list import LinkedList

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

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        current = self
        while current != None:
            value = current.value
            if value == target:
                return True
            elif value > target:
                current = current.left
            else:
                current = current.right

    def get_max(self):
        max_leaf = self
        while max_leaf.right != None:
            max_leaf = max_leaf.right
        return max_leaf.value

    def for_each(self, fn):
        fn(self.value)
        if self.left != None:
            self.left.for_each(fn)
        if self.right != None:
            self.right.for_each(fn)

    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print(self.left)
        print(node)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        q = Queue()
        q.enqueue(self)

        while q.__len__() > 0:
            current_node = q.dequeue()
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)
            print(current_node.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        s = Stack()
        s.push(self)

        while s.__len__() > 0:
            current_node = s.pop()
            if current_node.left:
                s.push(current_node.left)
            if current_node.right:
                s.push(current_node.right)
            print(current_node.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node=None):
        if node == None:
            return
        print(node.value)
        if node.left != None:
            node.left.pre_order_dft(node.left)
        if node.right != None: 
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        if node == None:
            return
        
        if node.left != None:
            node.left.post_order_dft(node.left)
        if node.right != None:
            node.right.post_order_dft(node.right)

        print(node.value)

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