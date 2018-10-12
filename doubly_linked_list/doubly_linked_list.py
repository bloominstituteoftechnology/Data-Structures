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
    if self.count == 0:
            raise RuntimeError("Cannot pop from an empty linked list")
        result = self.head.value
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.current = self.head
        self.count -= 1
        return result

  def add_to_tail(self, value):
    if self.count == 0:
            self.add_to_head(0)
        else:
            self.tail.next = self.Node( self, value, next=None, self.tail )
            self.tail = self.tail.next
            self.count += 1

  def remove_from_tail(self):
    if self.count == 0:
            raise RuntimeError("Cannot pop from an empty linked list")
        result = self.tail.value
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return result

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
