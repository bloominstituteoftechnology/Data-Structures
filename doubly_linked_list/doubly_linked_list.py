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
    #create new node
    new_node = ListNode(value)

    #set the tail of the new node to old head
    new_node.next = self.head
    #set head to tail of new node
    self.head = new_node

    #if there is no head
    if self.head is None:
      #set head and tail to new listnode
      self.tail = new_node

  def remove_from_head(self):
    if self.head is not None:
      del_head = self.head.value
      new_head = self.head.next
      #delete head
      self.head.delete()
      #set next to new head
      self.head = new_head
      return del_head

  def add_to_tail(self, value):
    #create new node
    new_node = ListNode(value)

    #set the head of new node to old tail
    new_node.prev = self.tail
    #set new node as tail of list
    self.tail = new_node



  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    #prev.next should equal next.prev
    if node.prev is not None: 
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
    
