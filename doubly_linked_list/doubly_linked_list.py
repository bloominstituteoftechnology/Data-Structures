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
    # create "ListNode" w/value
    node = ListNode(value, None, self.head)
    # empty list
    if self.head == None and self.tail == None:
      self.head = node
      self.tail = node
      self.head.prev = None
      self.head.next = None
      self.length = 1
    else:
      self.head.prev = node
      node.prev = None
      self.head = node
      self.length += 1

  def remove_from_head(self):
    removed = self.head.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.lenght = 0
    else:
      self.head = self.head.next
      self.head.prev.delete()
      self.lenght -= 1
    return removed

  def add_to_tail(self, value):
    #similar to single linked list
    new_tail = ListNode(value, self.tail)
    if self.head == None and self.tail == None:
      self.head = new_tail
      self.tail = new_tail
      self.head.prev = None
      self.head.next = None
      self.length = 1
    else:
      self.tail.next = new_tail
      self.tail = new_tail
      self.length += 1
  

  def remove_from_tail(self):
    removed_node = self.tail.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.tail = self.head.prev
      self.tail.next.delete()
      self.length -= 1
    return removed_node

  def move_to_front(self, node):

    # remove 'node' ...ListNode delete() BUT need to save value first
    value = node.value # value = 2
    node.delete()
   
    # add 'node' to head ...add_to_head()
    self.add_to_head(value)

    pass

  def move_to_end(self, node):
    # similar to move_to_head()
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    cur_max = self.head.value
    cur_node = self.head
    # loop through nodes until reach tail
    while cur_node.next:
      cur_node = cur_node.next
    # if we find a node > cur_max, update 
      if cur_node.value > cur_max:
        cur_max = cur_node.value

    return cur_max

    pass
