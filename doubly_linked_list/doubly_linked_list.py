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

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.count = 0

  def add_to_head(self, value):
    if self.count == 0:
            self.head = self.ListNode( self, value, prev=None, next=None )
            self.tail = self.head
        elif self.count > 0:
            # create a new node pointing to self.head
            node = self.Node( self, value, prev=None, self.head )
            # have self.head point back to the new node
            self.head.prev = node
            # finally point to the new node as the self.head
            self.head = node
        self.current = self.head
        self.count += 1

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
