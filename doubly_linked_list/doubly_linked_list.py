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
  # `add_to_head` replaces the head of the list with a new value that is passed in.
    #increase length by 1
    self.length += 1

    # if Linked List is empty
    if not self.head and not self.tail:
      # Run ListNode and set head and tail
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node

    else:
      #Run insert_before from the node head and set head reference
      self.head.insert_before(value)
      self.head = self.head.prev
    
  def remove_from_head(self):
  # `remove_from_head` removes the head node and returns the value stored in it.

    # Empty Linked List Check
    if not self.head and not self.tail:
      return None

    if self.length > 0:
      # value = self.head.value
    # Check to see if only 1 node in Linked List
      if self.head == self.tail:
        value = self.head.value
        self.head = None
        self.tail = None
        self.length -= 1
        return value

      # If more than 1 node in Linked List
      else:
        value = self.head.value
        self.head.delete()
        return value

  def add_to_tail(self, value):
  # `add_to_tail` replaces the tail of the list with a new value that is passed in.
    #increase length by 1
    self.length += 1

    # if Linked List is empty
    if not self.head and not self.tail:
      # Run ListNode and set head and tail
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node

    else:
      # Run insert after from node tail and set tail reference
      self.tail.insert_after(value)
      self.tail = self.tail.next

  def remove_from_tail(self):
  # `remove_from_tail` removes the tail node and returns the value stored in it.

  # Empty Linked List Check
    if not self.head and not self.tail:
      return None

    if self.length > 0:
      # value = self.head.value
    # Check to see if only 1 node in Linked List
      if self.head == self.tail:
        value = self.tail.value
        self.head = None
        self.tail = None
        self.length -= 1
        return value

      # If more than 1 node in Linked List
      else:
        value = self.tail.value
        self.tail.delete()
        return value

  def move_to_front(self, node):
  # `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 

    # grab node value and delete node
    value = node.value
    self.delete(node)

    #add 'node' to head
    self.add_to_head(value)

  def move_to_end(self, node):
  # `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 

    # grab node value and delete node
    value = node.value
    self.delete(node)

    #add 'node' to tail
    self.add_to_tail(node.value)


  def delete(self, node):
  # `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.

    # Check to see if length is not 0.  Then delete node and -1 to Linked List length
    if self.length > 0:
      node.delete()
      self.length -= 1

    # Check to see if deleted node is head.  If so move head forward 1 node.
    if self.head == node:
      self.head = node.next

    # Check to see if deleted node is tail.  If so move tail behind 1 node.
    if self.tail == node:
      self.tail = node.prev

  def get_max(self):
  # `get_max` returns the maximum value in the list. 

    # if Linked List is empty return None
    if not self.head and not self.tail:
      return None

    else:
      #Set values for head node and head node value
      cur_max = self.head.value
      cur_node = self.head

      while cur_node.next:
        # while Linked List continues through itself
        cur_node = cur_node.next
        
        # Check to see if current nodes value is higher than the previous max value
        if cur_node.value > cur_max:
          cur_max = cur_node.value
      
      return cur_max