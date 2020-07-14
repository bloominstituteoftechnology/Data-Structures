# test_reverse.py
import unittest
from singly_linked_list import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_reverse_empty(self):
        self.list.reverse()
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)

    def test_reverse_single(self):
        self.list.add_to_tail(1)
        self.list.reverse()
        self.assertEqual(self.list.head.value, 1)
        self.assertEqual(self.list.tail.value, 1)

    def test_reverse_double(self):
        self.list.add_to_tail(1)
        self.list.add_to_tail(2)
        self.list.reverse()
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.tail.value, 1)

    def test_reverse_multi(self):
        self.list.add_to_tail(1)
        self.list.add_to_tail(2)
        self.list.add_to_tail(3)
        self.list.add_to_tail(4)
        self.list.add_to_tail(5)
        self.list.reverse()
        self.assertEqual(self.list.head.value, 5)
        self.assertEqual(self.list.tail.value, 1)
        node = self.list.head.next_node
        self.assertEqual(node.value, 4)
        node = node.next_node
        self.assertEqual(node.value, 3)
        node = node.next_node
        self.assertEqual(node.value, 2)
        node = node.next_node
        self.assertTrue(node is self.list.tail)


if __name__ == '__main__':
    unittest.main()
