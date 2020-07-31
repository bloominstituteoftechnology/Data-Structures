import unittest
import random
import sys
import io
from binary_search_tree import BSTNode
# from collections import deque
# class BSTNode:
#     def __init__(self, value):
#         # current node's value
#         self.value = value

#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         # check whether new node's value is less than current node's value
#         if value < self.value:
#             if not self.left:
#                 self.left = BSTNode(value)
#             else:
#                 self.left.insert(value)
#         # check whether new node's value is greater than or equal to curr node's val
#         elif value >= self.value:
#             if not self.right:
#                 self.right = BSTNode(value)
#             else:
#                 self.right.insert(value)


#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         # check whether curr node matches target
#         if self.value == target:
#             return True
#         if target < self.value:
#             if not self.left:
#                 return False
#             else:
#                 return self.left.contains(target)
#         else:
#             if not self.right:
#                 return False
#             else:
#                 return self.right.contains(target)

#     # Return the maximum value found in the tree
#     def get_max(self ):
#         #base case:
#         if not self.right:
#             return self.value
#         return self.right.get_max()

#         # if not self:
#         #     return None
#         # max_value = self.value
#         # current = self
#         # while current:
#         #     if current.value > max_value:
#         #         max_value = current.value
#         # return max_value


#     # Call the function `fn` on the value of each node
#     def for_each(self, fn):
#         fn(self.value)
#         if self.left:
#             self.left.for_each(fn)
#         if self.right:
#             self.right.for_each(fn)

#     # Part 2 -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self):
#         if not self:
#             return

#         if self.left:
#             self.left.in_order_print()

#         print(self.value)

#         if self.right:
#             self.right.in_order_print()

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self):
#         qq = deque()
#         qq.append(self)

#         while len(qq) > 0:
#             current = qq.popleft()
#             print(current.value)
#             if current.left:
#                 qq.append(current.left)

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self):
#         s = []
#         s.append(self)

#         while len(s) > 0:
#             current = s.pop()
#             print(current.value)
#             if current.left:
#                 s.append(current.left)



#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         if not self:
#             return
#         print(self.value)
#         if self.left:
#             self.left.pre_order_dft()
#         if self.right:
#             self.right.pre_order_dft()

#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         if not self:
#             return
#         if self.left:
#             self.left.post_order_dft()
#         if self.right:
#             self.right.post_order_dft()
#         print(self.value)

class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BSTNode(5)

    def test_insert(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(6)
        self.assertEqual(self.bst.left.right.value, 3)
        self.assertEqual(self.bst.right.left.value, 6)

    def test_handle_dupe_insert(self):
        self.bst2 = BSTNode(1)
        self.bst2.insert(1)
        self.assertEqual(self.bst2.right.value, 1)

    def test_contains(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertTrue(self.bst.contains(7))
        self.assertFalse(self.bst.contains(8))

    def test_get_max(self):
        self.assertEqual(self.bst.get_max(), 5)
        self.bst.insert(30)
        self.assertEqual(self.bst.get_max(), 30)
        self.bst.insert(300)
        self.bst.insert(3)
        self.assertEqual(self.bst.get_max(), 300)

    def test_for_each(self):
        arr = []
        cb = lambda x: arr.append(x)

        v1 = random.randint(1, 101)
        v2 = random.randint(1, 101)
        v3 = random.randint(1, 101)
        v4 = random.randint(1, 101)
        v5 = random.randint(1, 101)

        self.bst.insert(v1)
        self.bst.insert(v2)
        self.bst.insert(v3)
        self.bst.insert(v4)
        self.bst.insert(v5)

        self.bst.for_each(cb)

        self.assertTrue(5 in arr)
        self.assertTrue(v1 in arr)
        self.assertTrue(v2 in arr)
        self.assertTrue(v3 in arr)
        self.assertTrue(v4 in arr)
        self.assertTrue(v5 in arr)

    def test_print_traversals(self):
        # WARNING:  Tests are for Print()
        # Debug calls to Print() in functions will cause failure

        stdout_ = sys.stdout  # Keep previous value
        sys.stdout = io.StringIO()

        self.bst = BSTNode(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)

        # self.bst.in_order_print(self.bst)

        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n2\n3\n4\n5\n6\n7\n8\n")

        sys.stdout = io.StringIO()
        self.bst.bft_print(self.bst)
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n3\n7\n2\n4\n6\n" or
                        output == "1\n8\n5\n7\n3\n6\n4\n2\n")

        sys.stdout = io.StringIO()
        self.bst.dft_print(self.bst)
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n7\n6\n3\n4\n2\n" or
                        output == "1\n8\n5\n3\n2\n4\n7\n6\n")

        sys.stdout = io.StringIO()
        self.bst.pre_order_dft(self.bst)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n8\n5\n3\n2\n4\n7\n6\n")

        sys.stdout = io.StringIO()
        self.bst.post_order_dft(self.bst)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "2\n4\n3\n6\n7\n5\n8\n1\n")

        sys.stdout = stdout_  # Restore stdout

if __name__ == '__main__':
    unittest.main()
