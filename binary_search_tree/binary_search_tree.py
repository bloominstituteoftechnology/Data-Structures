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
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)
        else:
            return True

    def iter_print(self):
        stack = [self]
        while stack:
            n = stack.pop()
            if n.right:
                stack.append(n.right)
                print('right', n.right.value)
            if n.left:
                stack.append(n.left)
                print('left', n.left.value)

    def in_order(self):
        stack = []
        curr = self
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                break
            curr = stack.pop()
            print('value', curr.value)
            curr = curr.right

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        print(fn(self.value))
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        curr = self
        while curr:
            if node.value == curr.value:
                break
            elif curr.value > node.value:
                curr = curr.right
            elif curr.value < node.value:
                curr = curr.left
        stack = [curr]
        while stack:
            n = stack.pop()
            if n.right:
                print(n.right.value)
                stack.append(n.right)
            if n.left:
                print(n.left.value)
                stack.append(n.left)

            # Print the value of every node, starting with the given node,
            # in an iterative depth first traversal

    def dft_print(self, node):
        curr = self
        while curr:
            if node.value == curr.value:
                break
            elif curr.value > node.value:
                curr = curr.right
            elif curr.value < node.value:
                curr = curr.left
        stack = [curr]
        s = [curr.value]
        while stack:
            n = stack.pop()
            if n.right:
                stack.append(n.right)
                s.append(n.right.value)
            if n.left:
                stack.append(n.left)
                s.append(n.left.value)
        while s:
            print(s.pop(0))

            # Stretch Goals -------------------------
            # Note: Research may be required

            # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# bst.print_tree()
# print(bst.contains(55))
# bst.for_each(lambda x: x * 5)
# bst.print_tree()
# bst.dft_print(BSTNode(1))
# print(bst.get_max())
# bst.in_order()
