import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# insert value
# if there is no node at root - contains/find
# compare value to the root
# if value is smaller
    # look left if node exists repeat steps
    # if no node exists, make new one with this value
# if value is greater or equal
    # look right if node exisits repeat steps
    # if no node exists, make new one with this value


# if no root
# find value
# if no node at root, return false
# compare value to root
# if smaller
    # go left, look at node there
# if greater or ==:
    # go right

# the root in the binary search tree is the first in. 
# an unbalanced binary search tree can become a singly linked list. 
# time complexity to find somethingin tree is log(n)

# an avl tree is self-balancing. 

# get max is furthest right 
# if no right child, return value, otherwise go right

# a node and a tree are basically the same thing
# solvable without reference to paretn
# binary search trees leverages boolean logic, cutting list in half is a binary search
# big O is log base 2 because of computers being binary, partially because we're working in binary fashion
# the worst case scenario is an unbalanced binary search tree. 


# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         if self.value > value:
#             if self.left == None:
#                 self.left = BinarySearchTree(value)
#             else:
#                 self.left.insert(value)
#         elif self.value < value:
#             if self.right == None:
#                 self.right = BinarySearchTree(value)
#             else:
#                 self.right.insert(value)
#         elif self.value == value:
#             return "Tree already has value"
#         else:
#             return

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         if not value:
#             return False
#         if self.value ==target:
#             return True
#         if target > self.value:
#             if self.right:
#                 return self.right.contains(target)
#             else:
#                 return False
#         if target < self.value:
#             if self.left:
#                 return self.left.contains(target)
#             else:
#                 return False
#         else:
#             return


#     # Return the maximum value found in the tree
#     def get_max(self):
#         if self.right:
#             return self.right.get_max()
#         return self.value

#     # Call the function `cb` on the value of each node
#     # You may use a recursive or iterative approach
#     def for_each(self, cb):
#         if not self:
#             return
#         cb(self.value)
#         if self.left:
#             self.left.for_each(cb)
#         if self.right:
#             self.right.for_each(cb)

#     # DAY 2 Project -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self, node):
#         if not node:
#             return
#         self.in_order_print(node.left)
#         print(node.value)
#         self.in_order_print(node.right)

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self, node):
#         queue = Queue()
#         queue.enqueue(node)
#         values = ''
#         while queue:
#             curr = queue.dequeue()
#             if not curr:
#                 continue
#             values += str(curr.value) + '\n'
#             if curr.left:
#                 queue.enqueue(curr.left)
#             if curr.right:
#                 queue.enqueue(curr.right)
#         print(values[:-1])

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self, node):
#         stack = Stack()
#         stack.push(node)
#         values = ''
#         while stack:
#             curr = stack.pop()
#             if not curr:
#                 continue
#             values += str(curr.value) + '\n'
#             stack.push(curr.right)
#             stack.push(curr.left)
#         print(values[:-1])

#     # STRETCH Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self, node):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self, node):
#         pass


class BinarySearchTree:
    self.value = value 
    self.left = left_subtree
    self.right = right_subtree


    def insert(self, value):
        if self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            return "not a value"


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value: # otherwise if value is less than the node, go left
            if not self.left: # we look at the left, there's no children that are smaller
                return False # we're done
            else:
                return self.left.contains(target)
        else:
            if not self.right:# there's nothing found
                return False
            else:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right: # if there's something to the right
            return self.right.get_max()
        return self.value

        # max_value = self.value
        # current = self+
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb): # call the same function on every single node for the tree
        if not self:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)