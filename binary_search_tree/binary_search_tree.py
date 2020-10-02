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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
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

    def contains(self, target):

        if self.value == target:
            print(f"Made it with {target}")
            return True
        elif target < self.value and self.left:
            self.left.contains(target)
        elif target > self.value and self.right:
            self.right.contains(target)

        return False

        # def contains(self, target):
        # # check if the node is == target
        # if self.value == target:
        #     # if true return true
        #     return True
        # # otherwise check if target is < node value
        # elif target < self.value:
        #     # if left is None, target doesn't exist in tree, return false
        #     if self.left == None:
        #         return False
        #     # if left value is = target return true
        #     elif self.left.value == target:
        #         return True
        #     # otherwise move down left, call contains on left node
        #     else:
        #         self.left.contains(target)
        # # otherwise check if target is >= node value
        # elif target > self.value:
        #     # if right is None, target doesn't exist in tree, return false
        #     if self.right == None:
        #         return False
        #     # if right value is = target return true
        #     elif self.right.value == target:
        #         return True
        #     # otherwise move down right, call contains on right node
        #     else:
        #         self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        current_max = self.value
        current_node = self

        while current_node is not None:
            current_max = current_node.value
            current_node = current_node.right

        return current_max

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Recursive: place print statement in between recursive calls that explore left and right subtrees

        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        q = Queue()
        if self is None:
            return
        q.put(self)
        while q.empty() is not True:
            current = q.get()
            print(current.value)
            if current.left:

                q.put(current.left)
            if current.right:

                q.put(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        stack = []
        stack.append(self)

        while len(stack) is not 0:
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
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
tree = BSTNode(1)
tree.insert(8)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(3)
tree.insert(4)
tree.insert(2)

# tree.in_order_print()
# tree.bft_print()
tree.dft_print()
