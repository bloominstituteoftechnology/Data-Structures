"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __repr__(self):
    output = ""
    marker = self.head
    while marker:
      output += (f"{marker.value} -> ")
      marker = marker.next_node
    output += "None"
    return output

  def add_to_tail(self, value):
    new = Node(value, None)
    # if there is a tail, then set its next_node to the new node
    if self.tail:
      self.tail.next_node = new
    self.tail = new
    # if there is no head, then set the head to the new node
    if not self.head:
      self.head = new


  def remove_head(self):
    if not self.head:
      return None

    old_head = self.head
    self.head = old_head.next_node
    old_head.next_node = None
    if old_head == self.tail:
      self.tail = None

    if old_head:
      return old_head.value
    


  def contains(self, value):
    marker = self.head
    while marker:
      if marker.value == value:
        return True
      marker = marker.next_node
    return False

  def get_max(self):
    marker = self.head
    if not marker:
      return None
    max = marker.value
    while marker:
      if marker.value > max:
        max = marker.value
      marker = marker.next_node
    return max


linked = LinkedList()

linked.add_to_tail(10)
linked.add_to_tail(20)
print(linked.remove_head() == 10)
print(not linked.contains(10))
print(linked.remove_head() == 20)
print(not linked.contains(20))
print(linked)
print("\n")

linked.add_to_tail(10)   
print(linked) 
print(linked.remove_head() == 10)    
print(linked) 
print(linked.head == None)

print(linked.tail == None)
print(linked.remove_head() == None)