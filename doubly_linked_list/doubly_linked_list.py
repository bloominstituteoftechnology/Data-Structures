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
    # have to overwrite next and prev or else they'll be none type
    if self.head and self.tail:
      curr_head = self.head
      new_head = ListNode(value, None, curr_head) #new node adding to head
      self.head = new_head #setting pointer to the value of new node 
      # self.head.next = curr_head #setting pointer from new head to old head
      curr_head.prev = new_head
    else: #if the list is empty now theres one node
      self.head = ListNode(value)
      self.tail = self.head

  def remove_from_head(self):
    if self.head:
      curr_head = self.head
      if self.tail: 
        next = self.head.next
        self.head = next
        self.head.prev = None
      else: # if theres only one element in list then remove it
        self.head = None
        self.tail = None
    return curr_head.value

  def add_to_tail(self, value):
    # if nothings in the list 
    # if one elements in the list 
    # general
    curr_tail = self.tail
    node = ListNode(value)
    if self.head and self.tail:
      self.tail.next = node # creating new tail node
      self.tail = self.tail.next
    else: #only element
      self.head = node
      self.tail = self.head
    return curr_tail

  def remove_from_tail(self):
    if self.tail:
      curr_tail = self.tail # current tail
      curr_tail.delete()
      self.tail = curr_tail.prev
      return curr_tail.value

  def move_to_front(self, node):
    # move any node to the front
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node

  def delete(self, node):
    node.delete()
    # next_node = node.next 
    # prev_node = node.prev
    # prev_node.next = next_node
    # next_node.prev = prev_node

  def get_max(self):
    if self.head is None:
      return None
    max_val = self.head.value
    curr_node = self.head.next
    while curr_node is not None: 
      if curr_node.value > max_val:
        max_val = curr_node.value
      curr_node = curr_node.next
    return max_val
