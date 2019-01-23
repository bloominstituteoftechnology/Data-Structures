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
    add_node = ListNode(value)
    if self.head is None:
      self.head = add_node
    elif self.head is not None:
      curr_head = self.head.value
      self.head = add_node
      self.head.insert_after(curr_head)


  def remove_from_head(self):
    curr_head = self.head.value
    self.head.delete()
    return curr_head

  def add_to_tail(self, value):
    list_node = ListNode(value)
    if self.tail is None:
        self.tail = list_node
    else:
       prev_tail = self.tail
       self.tail = list_node
       self.tail.prev = prev_tail
       self.tail.insert_before(self.tail.value)

  def remove_from_tail(self):
    curr_tail = self.tail.value
    self.tail.delete()
    return curr_tail

  def move_to_front(self, node):
    prev_node = self.head
    self.head = node
    self.head.next = prev_node
    return self.head.value

  def move_to_end(self, node):
    next_node = self.tail
    self.tail = node
    self.tail.prev = next_node
    return self.tail.value

  def delete(self, node):
    pass
    
  def get_max(self):
    curr_max = 0
    curr_node = self.head

    while curr_node is not None:
      if curr_node.value > curr_max:
        curr_max = curr_node.value
      curr_node = curr_node.next
    return curr_max if curr_max > 1 else None