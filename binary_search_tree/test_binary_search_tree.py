import unittest
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

if __name__ == '__main__':
  unittest.main()
