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
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if the root contains the target value
        if target == self.value:
            return True

        # if target is less than self.value, target has to be on left
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        # if target is greater than self.value, target has to be on right
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Return the minimum value found in the tree
    def get_min(self):
        if self.left is None:
            return self.value
        return self.left.get_min()

    # Call the function `fn` on the value of each node
    # This method doesn't return anything
    def for_each(self, fn):

        # Depth-first Recursion
        # call fn on self.value
        fn(self.value)
        # check if self has a left child
        if self.left:
            # call for_each on the left child, passing in the fn
            self.left.for_each(fn)

        # check if self has a right child
        if self.right:
            # call for_each on the right child, passing in the fn
            self.right.for_each(fn)

        # # Depth-first iterative: LIFO
        # # How do we achieve the same ordering that recursion gave us for free?
        # # Use a stack to achieve the same ordering
        #
        # stack = []
        # # add the root node to our stack
        # stack.append(self)
        #
        # # continue popping from our stack so long as there are nodes in it
        # while len(stack) > 0:
        #     current_node = stack.pop()
        #
        #     # check if this node has children
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
        #
        #     fn(current_node.value)
        #
        #
        # Breadth-First Traversal (level by level)
        # from collections import deque
        #
        # q = deque()
        # q.append(self)
        #
        # while len(q) > 0:
        #     current_node = q.popleft()
        #
        #     # check if this node has children
        #     if current_node.left:
        #         q.append(current_node.left)
        #     if current_node.right:
        #         q.append(current_node.right)
        #
        #     fn(current_node.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self):
        # LEFT -> NODE -> RIGHT
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        q = deque()
        # pass in self instead of node to start from the root
        q.append(node)

        while len(q) > 0:
            current_node = q.popleft()

            # check if this node has children
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        # add the root node to our stack
        stack.append(node)

        # continue popping from our stack so long as there are nodes in it
        while len(stack) > 0:
            current_node = stack.pop()

            # check if this node has children
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        #  NODE -> LEFT -> RIGHT
        print(self.value)

        if self.left:
            self.left.pre_order_dft()

        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # LEFT -> RIGHT -> NODE

        if self.left:
            self.left.post_order_dft()

        if self.right:
            self.right.post_order_dft()

        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(10)

bst.insert(7)
bst.insert(6)
bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(11)
bst.insert(20)
bst.insert(14)
bst.insert(22)

#  bft_print & dft_print won't work without passing in a node,
#  otherwise, change is to take self in the function
# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_print()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_print()
