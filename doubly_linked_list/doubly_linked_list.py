# Implemented by Ben Hakes

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
    
    new_head = ListNode(value,None,self.head)
    
    if self.head is None:
      self.head = new_head
      self.tail = new_head
      self.length = 1
    else:
      self.head.prev = new_head
      self.head = new_head
      self.length += 1

  def remove_from_head(self):
    if self.head is None:
      return
    elif self.head.next is None:
      head_to_return = self.head
      self.head = None
      self.tail = None
      self.length = 0
      return head_to_return.value
    else:
      head_to_return = self.head
      new_head = self.head.next
      self.head = new_head
      new_head.prev = None
      self.length -= 1
      return head_to_return.value

  def add_to_tail(self, value):
    new_tail_node = ListNode(value, None, None)

    if self.tail is None:
      self.tail = new_tail_node
      self.head = new_tail_node
      self.length = +1
    else:
      new_tail_node.prev = self.tail
      self.tail.next = new_tail_node
      self.tail = new_tail_node
      self.length += 1
      
  def remove_from_tail(self):
    if self.tail is None:
      return
    elif self.tail.prev is None:
      node_to_remove = self.tail
      self.tail.delete()
      self.length -= 1
      self.head = None
      self.tail = None
      return node_to_remove.value
    else:
      node_to_remove = self.tail
      self.tail.delete()
      self.length -= 1
      return node_to_remove.value

  def move_to_front(self, node):
    if self.head is None:
      self.add_to_head(node.value)
    elif self.head.next is None:
      if self.head == node:
        return
      else:
        self.head = node
        self.tail = node
    else:
      self.add_to_head(node.value)
      node.delete()
      self.length -= 1

  def move_to_end(self, node):
    if self.tail is None:
      self.add_to_tail(node.value)
    elif self.tail.prev is None:
      self.add_to_tail(node.value)
    elif self.head == node:
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1
      self.add_to_tail(node.value)
    else:
      node.delete()
      self.length -= 1
      self.add_to_tail(node.value)
  
      
    
  def delete(self, node):
    if self.head is None and self.tail is None:
      return 
    elif self.head.next is None:
      node.delete()
      self.head = None
      self.tail = None
      self.length = 0
    elif self.head == node:
      self.head = node.next
      node.delete()
      self.length -= 1
    elif self.tail == node:
      self.tail = node.prev
      node.delete()
      self.length -= 1
    else:
      node.delete()
      self.length -= 1
    
  def get_max(self):
    max_value = None
    if self.head is None:
      return -1
    else:
      node_to_check = self.head
      max_value = self.head.value
      while node_to_check.next is not None:
        node_to_check = node_to_check.next
        if node_to_check.value > max_value:
          max_value = node_to_check.value
      return max_value

        

