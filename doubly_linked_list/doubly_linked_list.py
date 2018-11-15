class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    # set the new node as a new ListNode

    # set the current node to this node

    # set the previous_node to the current nodes prev

    # set the other node to the current node next

    # set the previous of the new node to the current node

    # set the prev of the new node to the next node

    # set the next node of the current node to the new node
    pass

  def insert_before(self, value):
    # set the new node as a new ListNode
    # set the new nodes prev to the nodes prev
    # set new nodes next to this node
    # set this prev to the new node
    pass

  def delete(self):
    pass

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    pass

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
