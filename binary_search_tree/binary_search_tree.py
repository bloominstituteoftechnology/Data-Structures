"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class. DUE TUESDAY
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class. DUE THURSDAY
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    # search something

    def contains(self, target):
        # if (compare) target_value to cur_value
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

        # == we return true
        # < we go left
        # > we go right
        # if we cant go left/right return "false"
        # pass

    # Return the maximum value found in the tree
    def get_max(self):
        # go right -->
        max_node = self.value
        if self.right is None:
            return max_node
        else:
            return self.right.get_max()

        # pass

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # Recursive case
        fn(self.value)
        if self.left is not None:  # if there IS a left node (self.left)
            self.left.for_each(fn)  # procress each value pointing left
        if self.right is not None:
            self.right.for_each(fn)

        # base case - no more nodes in our subtree
        # cur_node = self
        # fn(cur_node.value)
        # stack = # codeHere: node you need to backtrack too
        # while cur_node.self:
        #     cur_node = cur_node.left
        #     fn(cur_node)
            # codeHere: add it to the stack
        # codeHere: pop off the stack
        # cocodeHerede: try to go 'right'

    # def delete(self, fn):
    #     if fn == self.value:
    #         return True
    #     elif fn < self.value and self.left:
    #             return self.left.delete(fn)
    #     elif fn > self.value and self.right:
    #             return self.right.delete(fn)
        # search like we did in contains()
        # different cases
        # if node at bottom level
        # update parent left/right = None
        # if node has only child
        # parent.left/right = node.left/right
        # if node has 2 children
        # "larger" child becomes the parent of its sibling

        # pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # left, parent, right
    def in_order_print(self, node=None):
        if node and node.left:
            return node.in_order_print(self.left)
        if node and node.right:
            return node.in_order_print(self.right)

            # go left (recursion function call)!

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # pre-Order , queue stack

    def bft_print(self, node=0):

        if node == None:
            return self.value
        else:
            cur_node = node
            queue = [cur_node]
        if self.value == None:
            return queue
        while queue:
            cur_node = queue.pop(0)
            print(self.value)
            # Return an iterator yielding those
            # items of iterable for which function(item) is true.
            # If function is None, return the
            # items that are true.

        # use a queue !
        # print current node, add left child to queue, add right child to queue
        # if not None
        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack : queue FILO
        stack = []
        # push some initial value(s) onto the stack
        stack.append(self)  # self == node value
        while len(stack) > 0:
            # pop a Node on top off stack to traverse its L & R children
            current_node = stack.pop()
            #  print value
            print(current_node.value)
            # push L & R child
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

    # Stretch Goals ---------------------------------------------------------------------
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
