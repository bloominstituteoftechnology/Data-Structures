# Queue implementation with (doubly)linked lists

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

  def remove_from_head(self):
    if self.__len__() > 0:
      ret = self.head.value
      self.head.delete()
      self.length -= 1
      if self.length == 0:  # no nodes left
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next
      return ret

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

  def get_len(self):
    return self.__len__()
    
class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = DoublyLinkedList()

  def __str__(self):
    return f"{self.storage}"

  def enqueue(self, item):
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    if self.storage.get_len() > 0:
      return self.storage.remove_from_head()

  def len(self):
    return self.storage.get_len()

'''
queue = Queue()

queue.dequeue()

queue.enqueue(5)
queue.enqueue(8)
queue.enqueue(13)

print(queue.len())

queue.dequeue()

print(queue.len())

queue.enqueue(5)
queue.enqueue(8)

print(queue.len())

queue.dequeue()

print(queue.len())
'''