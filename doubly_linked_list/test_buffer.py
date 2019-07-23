import unittest
from doubly_linked_list import DoublyLinkedList
from text_buffer import TextBuffer

class TextBufferTests(unittest.TestCase):
  def setUp(self):
    self.buf = TextBuffer('hello')
  
  def test_init(self):
    self.assertEqual(len(self.buf.contents), 5)
  
  def test_append(self):
    self.buf.append(' world!')
    self.assertEqual(self.buf.contents.head.value, 'h')
    self.assertEqual(self.buf.contents.tail.value, '!')
    self.assertEqual(len(self.buf.contents), 12)
  
  def test_prepend(self):
    self.buf.prepend('I say ')
    self.assertEqual(self.buf.contents.head.value, 'I')
    self.assertEqual(self.buf.contents.tail.value, 'o')
    self.assertEqual(len(self.buf.contents), 11)
  
  def test_delete_front(self):
    self.buf.append(' world!')
    self.buf.delete_front(6)
    self.assertEqual(self.buf.contents.head.value, 'w')
    self.assertEqual(self.buf.contents.tail.value, '!')
    self.assertEqual(len(self.buf.contents), 6)
  
  def test_delete_back(self):
    self.buf.append(' there, I am from Lambda School')
    self.buf.delete_back(7)
    self.assertEqual(self.buf.contents.tail.value, 'a')
    self.assertEqual(len(self.buf.contents), 29)
  
  def test_join_other_buffer(self):
    other_buf = TextBuffer(' world!')
    self.buf.join(other_buf)
    self.assertEqual(self.buf.contents.head.value, 'h')
    self.assertEqual(self.buf.contents.tail.value, '!')
    self.assertEqual(len(self.buf.contents), 12)
    
  def test_join_string(self):
    string = ' i am a string?'
    self.buf.join_string(string)
    self.assertEqual(self.buf.contents.head.value, 'h')
    self.assertEqual(self.buf.contents.tail.value, '?')
    self.assertEqual(len(self.buf.contents), 20)

if __name__ == '__main__':
  unittest.main()