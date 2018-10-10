import unittest
from linked_list import LinkedList

class LinkedListTests(unittest.TestCase):
  def setUp(self):
    self.list = LinkedList()

  def test_add_to_tail(self):
    self.list.add_to_tail(1)
    self.assertEqual(self.list.tail.value, 1)
    self.assertEqual(self.list.head.value, 1)
    self.list.add_to_tail(2)
    self.assertEqual(self.list.tail.value, 2)
    self.assertEqual(self.list.head.value, 1)

  
if __name__ == '__main__':
  unittest.main()
