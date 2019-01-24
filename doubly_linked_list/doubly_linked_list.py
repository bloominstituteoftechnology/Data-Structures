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
    # create a new node
    node = ListNode(value)
    # set tail of new to old head
    node.next = self.head
    # set head to new node
    self.head = node
    # if head is none
    if self.head is None:
      self.tail = node
      # set tail as well as head | new node
    pass

  def remove_from_head(self):
    # save head in temp
    # save head.next in temp
    # set head to temp
    # set head.prev to none
    # if self.head is none del tail | set tail to none
    # return removed value
    pass

  def add_to_tail(self, value):
    # create a new node
    # if tail is not none
      # save tail in temp
      # set tail.next to new node
      # set new node.prev to temp tail
    # if tail is none
      # set head to new node
    # set self.tail to new node
    pass

  def remove_from_tail(self):
    # if tail not none
    # save current tail for return
    # set tail as tail.prev
    # set tail.next to none
    pass

  def move_to_front(self, node):
    # save head in temp
    # node.prev = node.next
    # if head is not none
      # set head.prev to node
      # node.prev set to none
      # node.next set to temp head
      # set head to node
    # head = node
    # tail = node
    pass

  def move_to_end(self, node):
    # save tail in temp
    # node.next = node.prev
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass