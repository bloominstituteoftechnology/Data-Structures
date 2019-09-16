import sys
#sys.path.append('../doubly_linked_list')
#from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.size += 1
    new_node = ListNode(value, None, None)
    if self.storage.head is None and self.storage.tail is None:
      self.storage.head = new_node
      self.storage.tail = new_node
    else:
      new_node.prev = self.storage.tail
      self.storage.tail.next = new_node
      self.storage.tail = new_node
      
  def dequeue(self):
    if self.storage.head is None:
      pass
    else:
      value = self.storage.head.value
      self.size -= 1
      if self.storage.head.next != None:
        self.storage.head.next.prev = None     
      self.storage.head = self.storage.head.next
      return value

  def len(self):
    return self.size











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
  
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""
  def add_to_head(self, value):
    pass
  
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    pass

  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    pass

  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    pass

  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    pass

  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    pass

  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    pass
    
  """Returns the highest value currently in the list"""
  def get_max(self):
    pass
