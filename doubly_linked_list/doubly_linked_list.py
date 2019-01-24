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
    nextent_next = self.next
    self.next = ListNode(value, self, nextent_next)
    if nextent_next:
      nextent_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    nextent_prev = self.prev
    self.prev = ListNode(value, nextent_prev, self)
    if nextent_prev:
      nextent_prev.next = self.prev

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
    if self.head is None:
      self.head = ListNode(value)
      self.tail = ListNode(value)
    else:
      new_node = ListNode(value)
      new_node.next = self.head
      new_node.prev = new_node
      self.head = new_node

  def remove_from_head(self):
    unwanted_node = self
    if self.head == None:
      return self.head
    else:
      ret_val = self.head.value
      self.head = self.head.next
      
      # if the head is none then set the tail to none and return the ret_val to the caller
      if self.head is None:
        self.tail = None

      return ret_val


  def add_to_tail(self, value):
    # set new node as a new list node with value
    new_node = ListNode(value)

    # set the prev of the new node to the nextent tail
    new_node.prev = self.tail

    # set the nextent tail to the next node with a value of the new node
    self.tail.next = new_node

    # if the head and the tail are none then set the head and tail to the new node
    if self.head is None and self.tail is None:
      self.tail = new_node
      self.head = new_node

    # otherwise just set the tail to the new node
    else:
      self.tail = new_node

  def remove_from_tail(self):
    node_to_remove = self.tail 
    
    # set the previous node to the previous node of the tail
    previous_node = self.tail.prev
    
    # set the next node of the previous node to none
    previous_node.next = None
    
    # set the nextent tail to the previous node and return the removal nodes value to the caller
    self.tail = previous_node
    return node_to_remove.value

  def move_to_front(self, node):
    node.delete
    self.add_to_head(node.value)

  def move_to_end(self, node):
    node.delete()
    self.add_to_tail(node.value)

  def delete(self, node):
    next_node = node.next 
    previous_node = node.prev
    # swap the 2 nodes (next node) and (previous node)
    previous_node.next = next_node
    next_node.prev = previous_node
    
  def get_max(self):
    max_val = -999999999
    cur_node = self.head
    while True:
      if cur_node is None:
        return None
      if cur_node.value > max_val:
        max_val = cur_node.value
      if cur_node.next == None:
        return max_val
      else:
        cur_node = cur_node.next


