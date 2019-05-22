# Garbage Collection
import gc


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
    new_node = ListNode(value)
    if self.head == None:
      """Check if there isn't a head, if so 
      - set new node to be the head and tail"""
      self.head = new_node
      self.tail = new_node
    else:
      """Else sex head to be the next node
      of the new node, and then set new node
      to the head."""
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    if self.head == None:
      """Early return: Check if a head exist,
      if not, return None"""
      return None
    # store the value to return
    old_head_value = self.head.value
    # old_head = self.head # and line 76
    self.head = self.head.next
    # set the previous none to none
    self.head.prev = None
    # Delete the old head
    # del(old_head)
    # check if there was only one node
    if self.head == None:
      self.tail = None
    
    # i don't have cover deleting the old
    # head in any of our examples.
    # I'll come back to this...
    # gc.collect()
    self.length -= 1
    return old_head_value

  def add_to_tail(self, value):
    """ Check if self.tail exist"""
    if self.tail == None:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      # create new node insert after tail
      self.tail.insert_after(value)
      # set new node to tail
      self.tail = self.tail.next
    self.lenght += 1

  def remove_from_tail(self):
    if self.tail == None:
      return None
    old_tail_value = self.tail.value
    self.tail = self.tail.prev
    self.tail.next = None
    # check if there was only one node
    if self.tail == None:
      self.head = None
    return old_tail_value


  def move_to_front(self, node):
    """ check if there is only one node in
    the list"""
    if self.head == self.tail:
      return
    if node == self.tail:
      self.tail = node.prev
    temp_value = node.value
    node.delete()
    # add the new node to the from of the list
    self.head.insert_before(temp_value)
    self.head = self.head.prev
    


  def move_to_end(self, node):
    if self.head == self.tail:
      return
    if node == self.head:
      self.head = node.next
    temp_value = node.value
    node.delete()
    # add the new node to the from of the list
    self.head.insert_after(temp_value)
    self.tail = self.tail.next

  def delete(self, node):
    # well this is kinda confusing...
    node.delete()
    
  def get_max(self):
    if self.head == self.tail:
      return
    current_max = None
    current_node = self.head
    while current_node:
      if not current_max or current_node.value > curent_max:
        current_max = current_node.value
      # traverse thru the list.
      current_node = current_node.next
