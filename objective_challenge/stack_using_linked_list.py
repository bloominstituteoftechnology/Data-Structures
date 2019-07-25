# Stack implementation with (doubly)linked lists

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

  def add_to_tail(self, value):
    if self.__len__() == 0:   # when the idiot wants to do this to a null dll
      node = ListNode(value)
      self.head = node
      self.tail = node
      self.length = 1
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.length += 1

  def remove_from_tail(self):
    if self.__len__() > 0:
      ret = self.tail.value
      self.tail.delete()
      self.length -= 1
      if self.length == 0:  # no nodes left
        self.head = None
        self.tail = None
      else:
        self.tail = self.tail.prev
      return ret

  def get_len(self):
    return self.__len__()
    
class Stack:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = DoublyLinkedList()

  def __str__(self):
    return f"{self.storage}"

  def push(self, item):
    self.storage.add_to_tail(item)
  
  def pop(self):
    if self.storage.get_len() > 0:
      return self.storage.remove_from_tail()

  def len(self):
    return self.storage.get_len()

'''
stack = Stack()

stack.pop()

stack.push(5)
stack.push(8)
stack.push(13)

print(stack.len())

print(stack.pop())

print(stack.len())

stack.push(5)
stack.push(8)

print(stack.len())

print(stack.pop())

print(stack.len())
'''