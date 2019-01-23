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

  def add_to_head(self, value):
    new_node = ListNode(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      print(self.head.value)
    

    

  def remove_from_head(self):
    if not self.head:
      return None
    if not self.head.next:
      x = self.head
      self.head = None
      self.tail = None
      return x.value
    cur_value = self.head.value
    self.head = self.head.next
    return cur_value

  def add_to_tail(self, value):
    new_node = ListNode(value)
    if not self.head:
      self.head = new_node
    elif not self.tail:
      self.tail = new_node
    else:
      new_node.prev = self.tail
      new_node.next = None
      self.tail = new_node
      
    

  def remove_from_tail(self):
    if not self.head:
      return None
    if not self.tail:
      return None
    elif self.tail:
      x = self.tail
      self.tail = None
      return x.value
    self.tail = self.prev
    

  def move_to_front(self, node):

    pass

  def move_to_end(self, node):
    if node.head is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node

    

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
