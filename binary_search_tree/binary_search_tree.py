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

from queue.queue import Queue
from stack.stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    # Insert the given value into the tree
    def insert(self, value):
        node = BSTNode(value)
        if value < self.value:
            # place to the left
            if self.left is None:
                self.left = node
            else:
                # recursion to apply insert on child
                self.left.insert(value)
        elif value >= self.value:
            # place to the right
            if self.right is None:
                self.right = node
            else:
                # recursion to apply insert on child
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target <= self.value:
            # search the left branch
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            # search the right branch
            if target > self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # start with the first node (or current)
        current = self
        # look at the right-side ONLY, b/c left side is smaller
        while current.right is not None:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    # go through all the nodes
    def for_each(self, fn):
        # run the function "fn", as if it's a "test" of the node
        fn(self.value)
        if self.left is not None:
            # applies the for_each method to the self.left node
            self.left.for_each(fn)
        if self.right is not None:
            # applies the for_each method to the self.right node
            self.right.for_each(fn)

    # Extra/not needed for assignment
    def delete(self, target):
        # locate the node (.contains)
        # if node has 0 children
            # update parent to point to None
        # if node has 1 child (self.right/left)
            # parent.left/right = node.left/right
        # if node has 2 children
            # parent points to node.right
            # node.right.left points to node.left
        pass

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            if node.left:
                node.in_order_print(node.left)
            print(node.value)
            if node.right:
                node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.right:
                queue.enqueue(current_node.right)
            if current_node.left:
                queue.enqueue(current_node.left)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
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

# bst.bft_print()
# bst.dft_print()

print("elegant methods")
print("pre order")
# bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
# bst.post_order_dft()
