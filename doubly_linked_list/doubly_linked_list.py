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
    # My attempt using provided methods:
    # new_node = ListNode(value)
    # if not self.head:
    #   self.head = new_node
    #   self.tail = new_node
    # new_node.insert_before(self.head.value)


    # Instructor Solution:
    new_node = ListNode(value)
    # set the tail of new node to old head
    new_node.next = self.head
    # set head to the tail of new_node
    self.head = new_node  
    if not self.head:
      # set head and tail to new listnode
      self.head = new_node
      self.tail = new_node

  def remove_from_head(self):
    new_head = self.head
    removed_head = None
    if self.head:
      new_head = self.head.next
      if new_head:
        print('here', new_head.value)
        removed_head = self.head.value
        return removed_head
      self.tail = None
    return None

  def add_to_tail(self, value):
    new_tail = ListNode(value)
    if self.tail:
      self.tail.next = new_tail
    self.head = new_tail
    self.tail = new_tail

  def remove_from_tail(self):
    if self.tail:
      removed_tail = self.tail.value
      return removed_tail
    return None

  def move_to_front(self, node):
    print('beg', node.value)
    if node.prev:
      node.prev.next = node.prev
      print('here2', node.prev.value)
    self.head.prev = node
    node.next = self.head
    node.prev = None
    self.head = node
      

  def move_to_end(self, node):
    # Instructor Solution:
    # if node.prev:
    #   node.prev.next = node.next
    #   print('here', node.prev.value, node.next.value, node.prev.next.value)
    if node.next:
      node.next.prev = node.prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node

  def delete(self, node):
    pass
    
  def get_max(self):
    if self.head:
      curr_node = self.head.next
      max_value = self.head.value
      while curr_node:
        if curr_node.value > max_value:
          max_value = curr_node.value
        curr_node = curr_node.next
      return max_value
    return None
