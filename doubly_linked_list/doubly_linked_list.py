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
    self.max = node

  def add_to_head(self, value):
    node = ListNode(value)
    node.next = self.head
    node.prev = None

    if self.head is not None:
      self.head.prev = node
    self.head = node

    if node.value > self.max.value:
      self.max = node

  def remove_from_head(self):
    if self.head:
      temp = self.head
      temp.delete()
      self.head = temp.next
      return temp.value

  def add_to_tail(self, value):
    if self.tail is None:
      node = ListNode(value)
      self.tail = node
      if node.value > self.max.value:
        self.max = node
    else:
      node = ListNode(value, self.head)
      self.tail = node
      if node.value > self.max.value:
        self.max = node


  def remove_from_tail(self):
    if self.tail is not None:
      temp = self.tail
      temp.delete()
      self.tail = temp.prev
      return temp.value
      

  def move_to_front(self, node):
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    temp = node.value
    node.delete()
    self.head = self.head.next
    self.add_to_tail(temp)

  def delete(self, node):
    node.delete()
    
  def get_max(self):
    return self.max.value
