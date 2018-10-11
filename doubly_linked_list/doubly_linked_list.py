class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    pass

  def insert_before(self, value):
    pass

  def delete(self):
    pass

  def get_value(self):
    return self.value
  def get_next(self):
    return self.next 
  def set_next(self,new_next):
    self.next = new_next

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    pass

  def remove_from_head(self):
    if self.head == None:
        return self.head
    else:
      returning = self.head.get_value()
      self.head = self.head.get_next()
      if self.head is None:
          self.tail = None
      return returning 
      # get previous on head isn't needed because this isn't set 
      #up in a circular setting it was then if head was removed  previous
      #would be the tail so a connect with the new head and tail would have to be made.
      # because it is not a circle connection all other connections should be set.

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    """ just have to link out the node
    take the connect of the node and connect
    so left connection and right connection just needs to be 
    connected. 
    """
    pass
