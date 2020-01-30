import unittest
import random
import sys
import io
from binary_search_tree import BinarySearchTree


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree(5)

    def test_insert(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(6)
        self.assertEqual(self.bst.left.right.value, 3)
        self.assertEqual(self.bst.right.left.value, 6)

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

    def testMinimumvalue(self):
        self.assertEqual(self.bst.get_min(), 5)
        self.bst.insert(30)
        self.assertEqual(self.bst.get_min(), 5)
        self.bst.insert(300)
        self.bst.insert(3)
        self.assertEqual(self.bst.get_min(), 3)

    def testInorderSuccessor(self):
        my20 = self.bst = BinarySearchTree(20)
        my22 = self.bst.insert(22)
        my8 = self.bst.insert(8)
        my4 = self.bst.insert(4)
        my12 = self.bst.insert(12)
        my10 = self.bst.insert(10)
        my14 = self.bst.insert(14)

        self.assertEqual(my8.getInorderSuccessor(), 10)
        self.assertEqual(my4.getInorderSuccessor(), 8)
        self.assertEqual(my14.getInorderSuccessor(), 20)
        self.assertEqual(my10.getInorderSuccessor(), 12)
        self.assertEqual(my12.getInorderSuccessor(), 14)
        self.assertEqual(my20.getInorderSuccessor(), 22)
        self.assertEqual(my22.getInorderSuccessor(), None)

    def testInorderPredecessor(self):
        my20 = self.bst = BinarySearchTree(20)
        my22 = self.bst.insert(22)
        my8 = self.bst.insert(8)
        my4 = self.bst.insert(4)
        my12 = self.bst.insert(12)
        my10 = self.bst.insert(10)
        my14 = self.bst.insert(14)

        self.assertEqual(my8.getInorderPredecessor(), 4)
        self.assertEqual(my4.getInorderPredecessor(), None)
        self.assertEqual(my14.getInorderPredecessor(), 12)
        self.assertEqual(my10.getInorderPredecessor(), 8)
        self.assertEqual(my12.getInorderPredecessor(), 10)
        self.assertEqual(my20.getInorderPredecessor(), 14)
        self.assertEqual(my22.getInorderPredecessor(), 20)

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

        self.bst = BinarySearchTree(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)

        self.bst.in_order_print(self.bst)

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
