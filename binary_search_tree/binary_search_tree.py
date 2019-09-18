# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

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
        if value >= self.value:
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


bst = BinarySearchTree(5)
