# Implemented by Ben Hakes

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
    new_head = ListNode(value,None,self.head)
    self.head.prev = new_head
    self.head = new_head

  def remove_from_head(self):
    new_head = self.head.next
    self.head = new_head
    new_head.prev = None

  def add_to_tail(self, value):
    self.tail.insert_after(value)

  def remove_from_tail(self):
    self.tail.delete()

  def move_to_front(self, node):
    self.add_to_head(node.value)
    node.prev.next = node.next
    node.delete()

  def move_to_end(self, node):
    self.add_to_tail(node.value)
    node.prev.next = node.next
    node.delete()

  def delete(self, node):
    node.prev.next = node.next
    node.delete()
    
  def get_max(self):
    max_value = None
    if self.head is None:
      return -1
    else:
      node_to_check = self.head
      max_value = self.head.value
      while node_to_check.next is not None:
        node_to_check = node_to_check.next
        if node_to_check.value > max_value:
          max_value = node_to_check.value

        

