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
        # Check if the value is less than the current node's value
        if value < self.value:
            # Does the current node have a left child?
            if self.left is None:
                self.left = BSTNode(value)
            # Otherwise, it doesn't have a left child and we can park the new node here
            else:
                self.left.insert(value)
        # Otherwise, the value is greater than or equal to the current node's value
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return False

        # # Sean's way in lecture
        # # base case: check self's value to see if it matches the target
        # if self.value == target:
        #     return True
        # # otherwise, we need to go either left or right
        # # compare the target against self's value
        # if target < self.value:
        #     # base case: if there's no node here, then the target is not in the tree
        #     if not self.left:
        #         return False
        #     # otherwise, there is a node there:
        #     else:
        #         # call 'conatins' on the left child
        #         return self.left.contains(target)
        #         # base case: if there's no node here, then the target is not in the tree
        #         if not self.right:
        #             return False
        #         # otherwise, there is a node there:
        #         else:
        #             # call 'contains' on the right child
        #             return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # handle an empty BST
        if not self:
            return
        # handle a single-node BST
        if not self.right:
            return self.value
        # handle a multi-level BST
        else:
            return self.right.get_max()

        # # Sean's way in lecture:
        # # the max value is always going to be the rightmost tree node

        # # Recursive version:
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        # # Iterative version:
        # current = self
        # while current.right:
        #     current = current.
        # # we get to the point where 'current' doesn't have a right
        # return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self:
            return
        if self:
            fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=0):
        # Lowest number is always furthest to the left
        # Base case (if node is None)
        if node is None:
            return
        # Recursive case
        if node and node.left:
            return node.in_order_print(self.left)
        if node and node.right:
            return node.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        if self == None:
            return self.value
        # use a queue
        else:
            current = self
            queue = [current]
        if self.value == None:
            return queue
        # while loop that checks size of queue
        # using pointer variable that updates at the beginning of each loop
        while queue:
            current = queue.pop(0)
            print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # Use a stack
        stack = []
        # Start stack with root node
        stack.append(self)
        # Use a while loop that checks the size of the stack
        while len(stack) > 0:
            # pop a Node on top off stack to traverse its l/r children
            current = stack.pop()
            #  print value
            print(current.value)
            # push l/r chidren
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = deque()
        q.append(self)

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
    def dft_print(self):
        print(self.value)

        if self.right:
            self.right.dft_print()
        if self.left:
            self.left.dft_print()

#     # Stretch Goals -------------------------
#     # Note: Research may be required
#
#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         pass
#
#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         pass
#
# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)
#
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
#
# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
