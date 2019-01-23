class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

print('binary search tree ran')

bst = BinarySearchTree(5)
bst.insert(6)



# import unittest

# class BinarySearchTreeTests(unittest.TestCase):
#   def setUp(self):
#     self.bst = BinarySearchTree(5)

#   def test_insert(self):
#     self.bst.insert(2)
#     self.bst.insert(3)
#     self.bst.insert(7)
#     self.bst.insert(6)
#     self.assertEqual(self.bst.left.right.value, 3)
#     self.assertEqual(self.bst.right.left.value, 6)

#   def test_contains(self):
#     self.bst.insert(2)
#     self.bst.insert(3)
#     self.bst.insert(7)
#     self.assertTrue(self.bst.contains(7))
#     self.assertFalse(self.bst.contains(8))

#   def test_get_max(self):
#     self.assertEqual(self.bst.get_max(), 5)
#     self.bst.insert(30)
#     self.assertEqual(self.bst.get_max(), 30)
#     self.bst.insert(300)
#     self.bst.insert(3)
#     self.assertEqual(self.bst.get_max(), 300)

# if __name__ == '__main__':
#   unittest.main()