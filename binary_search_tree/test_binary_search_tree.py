import unittest
import random
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


if __name__ == '__main__':
  unittest.main()
