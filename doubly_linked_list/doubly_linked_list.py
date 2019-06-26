"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    node = ListNode(value)
    if self.head is not None:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      node = ListNode(value)
      self.head = node
      self.tail = node
    self.length += 1

  def remove_from_head(self):
    nextNode = self.head.next
    self.head.delete()
    self.head = nextNode
    self.length -= 1

  def add_to_tail(self, value):
    if self.tail is not None:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      node = ListNode(value)
      self.head = node
      self.tail = node
    self.length += 1

  def remove_from_tail(self):
    prevNode = self.tail.prev
    if self.head == self.tail:
      self.head.delete()
      self.tail.delete()

    self.tail.delete()
    self.tail = prevNode
    self.length -= 1

  def move_to_front(self, node):
    value = node.value
    node.delete()
    self.add_to_head(value)

  def move_to_end(self, node):
    value = node.value
    node.delete()
    self.add_to_tail(value)

  def delete(self, node):
    self.length -= 1
    node.delete()
    
  def get_max(self):
    max = self.head.value
    node = self.head
    if self.__len__() == 0:
      return 0
    else:
      while node is not None:
        node = node.next
        if node is None:
          break
        if node is not None and node.value > max:
          max = node.value
    return max


dll = DoublyLinkedList(ListNode(1))
dll.add_to_head(100)
dll.add_to_head(200)
dll.add_to_tail(500)
dll.remove_from_tail()
dll.remove_from_tail()
dll.remove_from_tail()
dll.remove_from_tail()
print(dll.head)
print(dll.tail)