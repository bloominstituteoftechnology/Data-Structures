class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.prev = prev
    self.value = value
    self.next = next
  
  def __repr__(self):
    return f"{self.value}"
  
  """Wrap the given value in a ListNode and insert it
  after this node. Note that this Node could already
  have a next node it is pointing to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next
  
  """Wrap the given value in a ListNode and insert it
  before this node. Note that this Node could already
  have a previous node it is pointing to."""
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


class Queue:
  def __init__(self):
    self.storage = {}

  def enqueue(self, item):
    if not self.head and self.tail:
      self.head = ListNode(item)
      self.tail = ListNode(item)
    else:
      current = self.head
      while(current):
        if(not current.next):
          ListNode.insert_after(item)
        current = current.next
  
  def dequeue(self):
    #if length is greater than 0, pop off the last item:
    if len(self.storage) > 0:
      return self.storage.pop(0)
    return None #return None when the length is 0

  def len(self):
    # return len(self.storage)
    return len(self.storage)
