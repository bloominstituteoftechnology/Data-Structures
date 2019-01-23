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
      self.head.prev = ListNode(value) #new node adding to head
      self.head = self.head.prev #setting pointer to the value of new node 
      self.head.next = curr_head #setting pointer from new head to old head
    else: #if the list is empty
      self.head = ListNode(value)
      self.tail = self.head

  def remove_from_head(self):
    if self.head:
      curr_head = self.head
      if self.tail: 
        next = self.head.next
        self.head = next
        self.head.prev = None
      else: # if theres only one element in list
        self.head = None
    return curr_head.value

  def add_to_tail(self, value):
    curr_tail = self.tail
    if self.head and self.tail:
      self.tail.next = ListNode(value) # creating new tail node
      self.tail = self.tail.next
    else: 
      self.head = None
    return curr_tail

  def remove_from_tail(self):
    if self.tail is None: # no elements in the list
      self.tail = None
      return self.tail.value
    else:
      curr_tail = self.tail # current tail
      self.tail = self.tail.prev 
      # self.tail.next = None 
      return curr_tail.value

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
