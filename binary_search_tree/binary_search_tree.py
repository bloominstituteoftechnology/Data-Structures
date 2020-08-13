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
from stack import Stack
from queue import Queue
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
        # check to see if it is the target is the value
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)

        return False


    # Return the maximum value found in the tree
    def get_max(self):
        # check to see if there is a right node
        if not self.right:
            # return the value
            return self.value
        # call the get max of right side
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node = None):
        # if self.left is None:
        #     if self.right:
        #         print(self.value)
        #         print(self.right.value)

        #     self.in_order_print()
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node = None):
        queue = Queue()
        if node:
            queue.enqueue(node)
        else:
            queue.enqueue(self)

        while len(queue) > 0:
            current_node = queue.dequeue()

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node = None):
        stack = Stack()
        if node:
            stack.push(node)
        else:
            stack.push(self)

        while len(stack) > 0:
            current_node = stack.pop()

            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)

            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required
    # In-order DFT
    def in_order_dft(self, node = None):
        pass

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node = None):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node = None):
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
bst.in_order_dft()
print("post order")
bst.post_order_dft()
