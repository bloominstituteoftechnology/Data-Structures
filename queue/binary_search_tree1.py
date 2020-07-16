from queue import Queue
from stack import Stack
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
        # Compare value to see if child should be left or right
        # Check if that child already exists, if so compare it by 
        # running that function again.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive
        if self.value is None:
            return

        fn(self.value) # apply the function at this level
        if self.left:
            self.left.for_each(fn) # if left exists run the function at that level

        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left) # This should get all the way down left
        print(node.value) # We are at the min 
        if node.right:
                self.in_order_print(node.right) # After all the left, check right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal. QUEUE
    def bft_print(self, node):
        # Use a queue to form a lin
        q = Queue()
        # for the nodes to get in
        # Start by placing root in queue
        q.enqueue(node)
        # Need a while loop to iterate, while len q>0
        while q.size > 0:
            # dequeue item from front of q
            node = q.dequeue()
            # print it
            print(node.value)
            # place current.left node if not none
            if node.left:
                q.enqueue(node.left)
            # place current.right in q if not None
            if node.right:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal. in order. STACK
    def dft_print(self, node):
        # initialize a stack
        s = Stack()
        # push root node onto stack
        s.push(node)
        # while loop stack.size > 0:
        while s.size > 0:
            # pop top item off
            node = s.pop()
            # Print value
            print(node)
            # if left, push
            if node.left:
                s.push(node.left)
            # if right, push
            if node.right:
                s.push(node.left)

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

bst.dft_print(bst)
