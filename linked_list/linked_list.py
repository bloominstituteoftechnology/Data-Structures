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

  def add_to_tail(self, value):
    new = Node(value)
    if self.tail is None:
      self.tail  = new
      self.head = new
    elif self.head == self.tail:
      self.head.set_next(new)
      self.tail = new
    else:
      self.tail.set_next(new)
      self.tail = new

  def remove_head(self):
    if self.head is None:
      print("no head")
    else:
      headprev = self.head.get_value()
      if self.head.get_next() is None:
        self.head = None
        self.tail = None
        return headprev
      else:
        self.head = self.head.get_next()
        print(headprev)
        return headprev

  # def contains(self, value):
  #   current = self.head
  #   match = False
  #   if current is None:
  #     return False
  #   elif current.get_value() == value:
  #     return True
  #   else:
  #     while match == False:
  #       if current.get_next() == None:
  #         return False
  #       else:
  #         current = current.get_next()
  #         if current.get_value() == value:
  #           match = True
  #           return True

  def contains(self, value, current="koolkats"):
    if current == "koolkats":
      current = self.head
    if current == None:
      return False
    elif current.get_next() == None and current.get_value() != value:
      return False
    elif current.get_value() != value:
      return self.contains(value, current.get_next())
    else:
      return True

  def get_max(self):
    if self.head is None:
      return None
    else:
      current = self.head
      max = self.head.get_value()
      while current:
        if current.get_value() > max:
          max = current.get_value()
          current = current.get_next()
        else:
          current = current.get_next()
      return max
