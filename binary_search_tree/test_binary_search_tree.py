import unittest
import random
import sys
import io
from binary_search_tree import BSTNode

class BSTNodeTests(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
