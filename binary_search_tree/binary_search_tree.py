from dll_stack import Stack
from dll_queue import Queue
import sys
# sys.path.append('../queue_and_stack')

# * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
#     There is a myriad of ways to perform tree traversal; in this case any of them should work.


class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key == value
        self.value = value
        self.left = None
        self.right = None

    # * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    def insert(self, value):
      # if value is less then current node
        if value < self.value:
            # next reference is none - insert, else - call insert on next node
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if value is greater then current node
        else:
            # next reference is none - insert, else - call insert on next node
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
      # current value = root
      # while value does not equal none
      #   if value == target return True
      #   elif value < target current = self.left
      #   else current = self.right
      # return False
        current = self
        while current != None:

            value = current.value
            if value == target:
                return True
            elif value > target:
                current = current.left
            else:
                current = current.right
            # print(current.value)

        return False

    # * `get_max` returns the maximum value in the binary search tree.
    def get_max(self):
        # grab furthest right leaf
        max_leaf = self
        while max_leaf.right != None:
            max_leaf = max_leaf.right
        return max_leaf.value

 # * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
    #     There is a myriad of ways to perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
      # for each node, run the function on the value and call the function for the left and right if they exist
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

  # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_dft(self, node):
        if node == None:
            return
        if node.left != None:
            node.left.in_order_dft(node.left)
        print(node.value)
        if node.right != None:
            node.right.in_order_dft(node.right)
        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):

        bft = Queue()
        bft.enqueue(node)
        # node = node
        while bft.size > 0:
            node = bft.dequeue()
            print(node.value)
            # node = None
            if node.left != None:
                bft.enqueue(node.left)
            if node.right != None:
                bft.enqueue(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        dft = Stack()
        dft.push(node)
        # node = node
        while dft.size > 0:
            node = dft.pop()
            print(node.value)
            # node = None
            if node.left != None:
                dft.push(node.left)
            if node.right != None:
                dft.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # print('per')
        if node == None:
            return
        print(node.value)
        if node.left != None:
            node.left.pre_order_dft(node.left)

        if node.right != None:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node == None:
            return

        if node.left != None:
            node.left.post_order_dft(node.left)

        if node.right != None:
            node.right.post_order_dft(node.right)

        print(node.value)

        # print(node.value)


bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
# bst.bft_print(bst)
# bst.dft_print(bst)
# bst.in_order_dft(bst)
bst.post_order_dft(bst)
